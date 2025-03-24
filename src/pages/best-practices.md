---
title: Best Practices for unitaryHACK Issues
date: 2025-03-20
metaDescription: Best Practices for unitaryHACK Issues
permalink: /best-practices/index.html
---

So you’re a maintainer of an open-source quantum software package – neato! And you’re participating in [unitaryHACK](https://unitaryhack.dev/) this year – huzzah!

This guide will help you create and curate issues on your GitHub repo that new contributors will be eager to work on and help reduce friction in the development process. 

[Jump to Best practices guide]({{ '/best-practices#best-practices-guide' | url }})

## Why should I read this?

You are an expert on your software project, but new people? Not so much. Allow me to illustrate with this [xkcd comic](https://xkcd.com/2501/):

<div style="text-align: center"><img style="display: inline-block; width: 300px" src="/assets/img/average_familiarity_2x.png" alt="How could anyone consider themselves a well-rounded adult without a basic understanding of silicate geochemistry? Silicates are everywhere! It's hard to throw a rock without throwing one!" /></div>
<br/>

You want high-quality contributors, right? You probably also want to help them get up and running while minimizing the time going back and forth, answering basic questions about your project.

The tips in this guide are good practice in general, but in particular in UnitaryHack, where people are competing to close issues with *cash bounties*, the stakes for creating a well-scoped issue are heightened. If you believe me, read on!

## Best practices guide

### 1. Add links to relevant source code and documentation

This is the biggest one: people don’t know what you’re talking about if you only use *words* (which may have a different meaning in the context of your project) or shorthand (people have different interpretations for the same acronyms). 

Luckily, Tim Berners-Lee invented [URL](https://en.wikipedia.org/wiki/URL) links! What a wondrous invention! Use them :) If you are referencing a section of your code, documentation, or another software package, add a link to it. Always err on the side of more links.

Good example of Best Practice 1:

[INSERT ]

### 2. Include a [Minimal Reproducible Example](https://stackoverflow.com/help/minimal-reproducible-example) (MRE)

If the issue is a bug, make sure to include a code snippet, script, or set of instructions that can reproduce the problem. Even if you don’t know exactly where an error is coming from, just understanding a normal workflow will help a contributor get up to speed at isolating and solving the problem.

Good example of Best Practice 2:

[INSERT ]

### 3. Define what’s in scope (and out of scope)

Estimate what is realistic to complete in the hacking period. Maybe what you really want is a full refactor of your entire plotting module, but in the short term, you just need your labels to stop overlapping. Make this clear in the issue, including the broader context if you think it’s relevant.

Good example of Best Practice 3:

[INSERT ]

### 4. Explain why it matters

What does this issue do for your project? Is it blocking something else from working? Would it be a speedup over your current workflow? Is it an implementation of a cool new paper?

Answering these questions will help a new person get a sense for why fixing this issue is a priority and gives their work meaning. 

Good example of Best Practice 4:

[INSERT ]

## General best practices (beyond UnitaryHack):

* Consider creating Github issue templates (check out [UCC for examples](https://github.com/unitaryfund/ucc/tree/main/.github/ISSUE_TEMPLATE)):
* These help the person submitting the issue scope it well from the start, e.g. including an MRE, explaining the context and alternatives considered, etc.

[INSERT EXAMPLES]

<img src="/assets/img/issue_templates.png" alt="When you define issue template files, they appear in the GitHub issue ticket web UI." />
<br/>

* Create informative, user friendly documentation.

Yeah yeah, docs are usually the last thing on our minds, and their development is not considered as sexy as contributing new features or getting a speedup, but can really help new people get up and running with your project, and will help new devs who want to contribute understand how their work fits into the broader repo.