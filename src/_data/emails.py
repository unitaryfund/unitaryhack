import json
import csv

with open("hackers.json") as f:
    hackers = json.load(f)

username_email_map = {}
username_name_map = {}
with open("signups.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for line in reader:
        if line["Email"]:
            username_email_map[line["GitHub Username"].lower()] = line["Email"]
        username_name_map[line["GitHub Username"].lower()] = line.get("Full Name")

for hacker in hackers:
    username = hacker["username"].lower()
    email = username_email_map.get(username)
    if not email:
        print(f"{username} DID NOT REGISTER!!!!!!!!!!!!!!!!!!")
    email_contents = (
        f"""{email}\n\n\nHey {username}!\n\nCongrats on a successful hackathon!"""
    )
    if len(hacker["bounties"]) > 1:
        email_contents += f""" We're so happy to see you were able to close {len(hacker["bounties"])} issues across {hacker["num_projects"]} projects. Here are the bounties we believe you should be rewarded for:\n\n"""
        for bounty in hacker["bounties"]:
            email_contents += (
                f'- [{bounty["title"]}]({bounty["url"]}): ${bounty["value"]}\n'
            )
        email_contents += "\n"
    else:
        bounty = hacker["bounties"][0]
        email_contents += f' Our records indicate you were responsible for closing "[{bounty["title"]}]({bounty["url"]})" worth \${bounty["value"]}. '

    email_contents += f"Hence, your total payout is **${hacker['total_value']}USD**! This information is also summarized at https://unitaryhack.dev/hackers/{username.lower()}/."
    email_contents += """ It's now time to get you paid! We'll need to collect some information from you in order to make this happen. Would you please submit a (single!) response to [this form](https://airtable.com/app5sTD1ailjCEft1/pagAP2GlpYyheivGA/form) at your earliest convenience? Once we have the necessary information, we can begin processing your payment."""

    with open(f"emails/{username}.md", "w") as f:
        f.write(email_contents)


for hacker in hackers:
    username = hacker["username"].lower()
    email = username_email_map.get(username)
    name = username_name_map.get(username)
    print(name, ",", username, ",", email)
    