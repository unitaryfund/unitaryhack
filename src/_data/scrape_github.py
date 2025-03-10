import json
import os
import re

import frontmatter
import github

g = github.Github(os.getenv("GH_TOKEN"))

PROJECT_PATH = "../projects"


def URL_to_repo_key(url: str) -> str:
    repo = re.match("^https:\/\/github\.com\/([\w-]*\/[^\/]*)\/?$", url)
    if repo:
        return repo[1]
    raise ValueError(f"did not find string match for {url}")


def get_project_info():
    for filename in os.listdir(PROJECT_PATH):
        if filename.endswith(".md"):
            yield frontmatter.load(os.path.join(PROJECT_PATH, filename))


projects = {}
for project in get_project_info():
    project_url = project["project_url"]
    main_project_repo_key = URL_to_repo_key(project_url)
    project_name = main_project_repo_key.split("/")[-1].lower()
    issue_list = []
    amount_available = 0
    total_bounty_amount = 0
    bounties = project.get("bounties", [])
    num_open_bounties = 0
    for bounty in bounties:
        total_bounty_amount += bounty["value"]
        repo_key = bounty.get("repo") or main_project_repo_key
        repo = g.get_repo(repo_key)

        issue_num = bounty["issue_num"]
        issue = repo.get_issue(number=issue_num)
        state = bounty.get("state") or issue.state
        if state == "open":
            amount_available += bounty["value"]
            num_open_bounties += 1
        extra_assignees = [bounty.get("assignee")] if bounty.get("assignee") else []
        issue_list.append(
            {
                "title": issue.title,
                "state": state,
                "assignees": list(
                    set([hacker.login for hacker in issue.assignees] + extra_assignees)
                ),
                "value": bounty["value"],
                "url": f"https://github.com/{repo_key}/issues/{issue_num}",
            }
        )

    projects[project_name] = {
        "name": project["title"],
        "emoji": project.get("emoji", ""),
        "url": project["project_url"],
        "bounties": issue_list,
        "amount_available": amount_available,
        "total_amount": total_bounty_amount,
        "num_bounties": len(bounties),
        "num_open_bounties": num_open_bounties,
    }

hack_stats = {
    "num_bounties": 0,
    "total_bounty_value": 0,
    "num_open_bounties": 0,
    "open_bounty_value": 0,
    "num_closed_bounties": 0,
    "closed_bounty_value": 0,
}

from collections import defaultdict

hackers = defaultdict(list)
for project, data in projects.items():
    for bounty in data["bounties"]:
        hack_stats["num_bounties"] += 1
        hack_stats["total_bounty_value"] += bounty["value"]
        hack_stats["num_open_bounties"] += 1 if bounty["state"] == "open" else 0
        hack_stats["open_bounty_value"] += (
            bounty["value"] if bounty["state"] == "open" else 0
        )
        hack_stats["num_closed_bounties"] += 1 if bounty["state"] == "closed" else 0
        hack_stats["closed_bounty_value"] += (
            bounty["value"] if bounty["state"] == "closed" else 0
        )
        if bounty["state"] == "closed":
            for hacker in bounty["assignees"]:
                hackers[hacker].append(
                    {
                        "url": bounty["url"],
                        "title": bounty["title"],
                        "project": project,
                        "value": int(bounty["value"] / len(bounty["assignees"])),
                    }
                )

hack_stats["num_hackers"] = len(hackers)

leaderboard = {hacker: len(bounties) for hacker, bounties in hackers.items()}
hacker_info = [
    {
        "username": hacker,
        "bounties": bounties,
        "num_projects": len(set(b["project"] for b in bounties)),
        "total_value": sum(b["value"] for b in bounties),
    }
    for hacker, bounties in hackers.items()
]

with open("hackers.json", "w") as f:
    json.dump(hacker_info, f, indent=2)

with open("leaderboard.json", "w") as f:
    json.dump(dict(sorted(leaderboard.items(), key=lambda hb: -1 * hb[1])), f, indent=2)

with open("gh.json", "w") as f:
    json.dump(projects, f, indent=2, sort_keys=True)

with open("stats.json", "w") as f:
    json.dump(hack_stats, f, indent=2)
