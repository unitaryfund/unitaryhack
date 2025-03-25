---
title: Project Maintainer Guide
metaDescription: Helpful information for project maintainers participating in unitaryHACK
date: 2025-03-21
permalink: /project-guide/index.html
eleventyNavigation:
  key: Maintainers
  order: 4
---

Our goal at Unitary Foundation is to build a quantum technology ecosystem that benefits the most people. That starts by **supporting and growing the great ecosystem of projects already out there that is maintained by awesome folks like you**.

It is always important for projects to find skilled and committed contributors that can do things like help develop new functionality, maintain existing tools, and write tests and documentation. This can be challenging in open source in general, but can be especially difficult for open source projects that need specialized skill sets like quantum computing. **unitaryHACK shows folks what amazing projects are already out there, helping drive quantum computing forward, and helping you find new contributions for your projects**.

We have some outlines below for what you can expect before and during the event, as well as [the rules for the event]({{ '/rules/' | url }}).

## Table of Contents
 - [Maintainer Timeline Quick Reference]({{ '/project-guide#%F0%9F%97%93%EF%B8%8F-maintainer-timeline-%F0%9F%97%93%EF%B8%8F' | url }})

 - [Before the HACK (March-April)]({{ '/project-guide#%E2%8C%9A-before-the-hack-%E2%8C%9A' | url }})
   - [Setting up your Github Repo]({{ '/project-guide#setting-up-your-github-repo' | url }})
   - [Choosing good issues for participants]({{ '/project-guide#how-to-choose-good-issues-for-participants' | url }})

 - [During the HACK (May 28 - June 11)]({{ '/project-guide#%F0%9F%9B%A0%EF%B8%8F-during-the-hack-%F0%9F%9B%A0%EF%B8%8F' | url }})

 - [Maintainer Tips and Tricks]({{ '/project-guide#maintainer-tips-and-tricks-during-the-hack' | url }})

 - [Frequently Asked Questions]({{ '/project-guide#%F0%9F%99%8B-faq-%F0%9F%A4%94' | url }})
   - [What will be expected of me/my team?]({{ '/project-guide#what-will-be-expected-of-me%2Fmy-team%3F' | url }})
   - [What does the maintainer workflow look like?]({{ '/project-guide#what-does-the-maintainer-workflow-look-like%3F' | url }})
   - [How much activity should we expect to see?]({{ '/project-guide#how-much-activity-should-we-expect-to-see%3F' | url }})
   - [What should I do if I have questions or need support?]({{ '/project-guide#what-should-i-do-if-i-have-questions-or-need-support%3F' | url }})

 - [Helpful Resources]({{ '/project-guide#%F0%9F%A4%9D-helpful-resources-%F0%9F%A4%9D' | url }})

## 🗓️ Maintainer Timeline 🗓️

> - **ASAP** Maintainers from invited projects fill out our [participation form](https://airtable.com/apppeZIiaDZ7dgNya/pagxR9MSOdmHEfALX/form)
> - **May 5th** Maintainers submit bounties for review
> - **May 23rd** All issues must be finalized
> - **May 23 at 9 am PT** Maintainers get together + Q&A
>   - Review of the event + rules
>   - Answer any initial questions folks have about the event
>   - Give a short intro about your project
> - **May 28th** unitaryHACK opens
> - **June 11th** unitaryHACK closes
> - **June 20th** Awardees finalized

## ⌚ Before the Hack ⌚

### Setting up your Github Repo

Get your project ready for more eyes on it! Some tips:

- If you have a `good first issue` label, it will be a good time to review it.
- Ensure you have `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` files at the root of your repo (or similar) so folks can learn how they should make their contributions.

In April, we will distribute a form to finalize which issues you'd like to put up for bounties, and the associated rewards associated. We will review the issues to make sure there is a good balance across the event. We are keeping the bounties hidden until the day of the event to ensure fairness.

### How to choose good issues for participants

To make sure that everyone can participate in the hackathon, we encourage project maintainers to tag a variety of issues that may or may not include quantum content, may or may not require devops skills, etc. We understand projects can be very targeted so if this is not possible that's totally fine! Our goal is to help connect eager and skilled contributors to your projects to help make the quantum open source ecosystem better 💖 We encourage you to reference our [Best practices for unitaryHACK Issues]({{ '/best-practices/' | url }}). for help in refining your issues to set contributors up for success.

## 🛠️ During the Hack 🛠️

As the hackathon progresses (and sometimes right away if there are eager folks who read up on the project), you should get some useful PRs! **If a PR does not meet a minimum bar for quality, or if another PR has been accepted, please provide some details through PR comments that it is not accepted.**

For bountied issues, once you have accepted a pull request (or closed an issue) please assign the hacker to the issue so that our bots can understand it as complete, and distribute the bounty accordingly. If multiple people will be splitting the bounty, assign multiple. **Bounties will not be distributed until the end of the event, so if there is any confusion, please don't hesitate to reach out** to [hack@unitary.fund](mailto:hack@unitary.fund).

## Maintainer Tips and Tricks During the HACK
- We recommend turning on github notifications for issue/PR events, so you can respond to activity as quickly as your bandwidth allows. The quicker hackers receive responses to their questions and/or PRs, the less confusion there is in general
- Stay active in the UF Discord server, specifically the unitaryHACK channel. You can easily share information there and quickly ask questions to the UF team 
- Reminder that a goal of unitaryHACK is to retain contributors to your projects. This is an opportunity to cultivate lasting relationships with the hackers so you can continue to work with them well into the future! 


## 🙋 FAQ 🤔

### What will be expected of me/my team?

In preparation for the hackathon, your project will need to file a series of bountied issues. These can range in difficulty, however they should be well scoped, and provide slightly more background than normal, so an external contributor with the right skills can get oriented quickly.

During the hackathon the expectation is that PRs opened by hackers are addressed in a reasonable time frame. Since many hackers are contributing on nights and weekends, giving feedback with ample time to make subsequent changes is very important.

### What does the maintainer workflow look like? 

Logistically, these are the steps a maintainer will take during the hackathon.

1. Hacker opens a PR on your project.
2. Maintainer reviews/requests changes as needed.
3. When PR is merged (or approved), maintainer assigns hacker to the bountied issue so our bots can understand who the bounty should be distributed to. In the cases where the bounty should be split, assign multiple hackers.

### How much activity should we expect to see?

In previous years we've seen some projects garner more attention, and some less. Generally, the more time you've taken to carefully select, scope, and detail issues to be put up for bounty, the more attention you should expect your project to see. Check out last year's [results](https://2024.unitaryhack.dev/bounties/) to get a more detailed sense.

### What should I do if I have questions or need support? 

Reach out to the UF team at [hack@unitary.fund](mailto:hack@unitary.fund). Or if you need to get to us even quicker, ping Veena on the UF Discord server. 

## 🤝 Helpful resources 🤝

- [A maintainers guide to Hacktoberfest](https://medium.com/gitcoin/a-maintainers-guide-to-hacktoberfest-21405c8ff09f)
- [Tips and tricks for maintaining your repo and your mental health](https://www.twilio.com/blog/how-to-hacktoberfest-tips-and-tricks-for-maintaining-your-repo-and-your-mental-health)
- [Promoting your open source project](https://github.com/zenika-open-source/promote-open-source-project/blob/master/README.md)
- [Write the docs guide](https://www.writethedocs.org/guide/)
