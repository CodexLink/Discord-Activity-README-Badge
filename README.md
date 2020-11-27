# A Discontinued Discord Bot to Incomplete Discord Bot Boilerplate

![Codacy Grade](https://img.shields.io/codacy/grade/d2da8866a48145be8c330a9056b35743?label=Codacy%20Code%20Quality&logo=codacy)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/CodexLink/dquerybotboilerplate?label=CodeFactor%20Code%20Quality&logo=codefactor)](https://www.codefactor.io/repository/github/codexlink/dquerybotboilerplate)

A boilerplate or template that utilizes Cogs in discord.py, along with OOP design patterns (just like in entrypoint file, trust me it works).


## Supporting Workflows / Proof of System Design

As of now, planning before coding is something that I have to normalize. Straight-up coding is not working for me anymore. Do you want to see how this program flows through? Both in the perspective of Bot and a Client? Then check this [drawio file.](https://drive.google.com/file/d/1ll6P6rstc5iTfRrKagBThs9yJgqGc9Wa/view?usp=sharing)

## Unintended Questions Answered

**Q1. What Happened Here?**

A1. This repo serves a redundant and useless feature. Technically, I don't need a bot to make things working. But rather I was too overwhelmed and excited to use Firebase for Rich Presence Caching and other such validators that may seem to be useful by the end of the day.

**However**, discord doesn't even get a downtime so there's **no need of cache**, and why do I need an **authentication** in the first place???? So firebase implementation is out of the way and the bot as well.

**Q2. What's gonna be the Approach since you have another repo about ProfileMD_DRP?**

A2. I will use the Docker Container File as an Action Workflow Service, but with a twist. I'm gonna use Python as I know the grasp and I know what it takes to do something in the Discord.py Library. (The proof is here.)

**Q3. Why don't you hide the repository because of ------ reason/s?**

A3. This repository might be potentially be a prime example of OOP implementation of the bot along with multiple COGs and dynamic load of extension (which is COGs).

**Q4. So, you're still going to update this one right???**

Q4. Yep, as long as I have a context and functionalities that may seem to be useful for a simple query bot. You can hit me up by making an Issue here, or if you have some changes, I would rather take the discussion in a PR form.

## Credits

During **pre-work** in progress stage, the list of links below helps me build some parts of the bot along with clarifications. This repository were not possible without the following guides, articles, documentations, tutorials, and whatever you call it.

* [Base PEP 3107 Example](https://github.com/ActivityWatch/aw-core/blob/master/aw_core/models.py) — An example models file that utilizes the PEP 3107.
* [Discord.py](https://github.com/athul/waka-readme) — Wakatime Weekly Metrics on your Profile Readme.
* [Discord Bot Examples](https://github.com/GreatTaku/Discord-Bot-Examples) — For Detailed Explanation of Particular Async Functions for handling events and response.
* [Simple Icons](https://simpleicons.org/) — SVG icons for popular brands.
* [PEP 8 Guidelines Tl;DR Version](https://realpython.com/python-pep8/#naming-conventions) — Huge thanks to [Jasmine Finer](https://github.com/jasminefiner) (who made the article) for TL;DR or compressed version of PEP 8 Guidelines.
* [Shields.io](https://shields.io/) — Concise, consistent, and legible badges in SVG and raster format.
* [StackOverflow Question: Discord bot that commits to github](https://stackoverflow.com/questions/61025429/discord-bot-that-commits-to-github) — Thanking the Answer OP for Concepts that I never thought, possible.
* [StackOverflow Question: Is OOP possible using discord.py without cogs?](https://stackoverflow.com/questions/63403758/is-oop-possible-using-discord-py-without-cogs) — Thanking the  OP for such question that I never thought will cross in my thoughts.
* [StackOverflow Question:](https://stackoverflow.com/questions/50981060/i-cant-add-commands-to-my-discord-bot-with-discord-py) — ???