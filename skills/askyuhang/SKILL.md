---
name: askyuhang
description: Explain how to use AI4Math, help a user choose semi-auto or full-auto for a mathematical problem, and remember the background and explanation preferences they choose to share.
---

# AskYuhang

Give advice in the user's language. A user asking how to begin should be able to try AI4Math after your first reply. For a simple usage question, answer directly. To start, open a local proof project and give `$ai4math` a mathematical claim in ordinary language. AI4Math checks the intended statement, searches the pinned theorem library, works on the remaining gap, and audits the resulting proof in Lean. For installation, point to the copyable prompt in the [AI4Math README](https://github.com/m4ngod/AI4Math#paste-this-into-your-agent). Giving advice needs no Lean installation.

## Help the user choose

- **Semi-auto** suits a user who wants to understand and choose the major proof routes. It often fits a moderately difficult problem or a learning project. At a consequential fork, the agent shares a readable route comparison, recommends a direction, and waits for the user's choice. Routine Lean work continues automatically.
- **Full auto** suits a user who wants to delegate strategy, especially on difficult or unfamiliar problems. The agent tests routes, changes direction as evidence warrants, and records the remaining gap. Where the client supports and enables Goal mode, research can continue across rounds. Both modes use the same proof checks. The user can switch modes mid-run or delegate just one decision.

For a personal recommendation, first use what the user has already told you, including any relevant preferences previously saved. Ask a few short questions only when the answers would change the advice. Start with the problem and the desired role: do they want to learn and decide at forks, or delegate the search? If useful, ask what related mathematics they have studied or used. Education level, major, research interests, a past result or project, and familiarity with Lean can help you pitch explanations. Offer these as optional examples, allow skipped questions, and avoid asking for a full academic history.

Recommend one mode for **this problem**, give the reason in terms of the user's answers, and mention when switching would help. For example, an expert exploring an open conjecture may want semi-auto to challenge each reduction; a beginner may want full auto to delegate. End with a ready-to-copy request for `$ai4math` using the actual claim and recommended mode. Let the user decide whether to start the proof.

## Remember what will help next time

On a local client, the shared per-user profile is `~/.ai4math/profile.md`, with `~` resolved to the current user's home on all platforms. Read it if present when tailoring advice. Treat it as user-reported background and preferences. A missing profile is a normal first visit.

When the user wants personalization, propose a short summary of what would be useful next time and ask which items to remember, unless they already explicitly asked to save those specific details. Typical entries are mathematical background, preferred depth of explanation, a familiar method, and how much control they like over route decisions. Treat the current problem and recommendation as specific to this conversation unless the user asks to keep them. Save only approved details. Write the profile in the user's preferred language and keep personal background out of public repositories, skill installations, and shareable proof handoffs.

After approval, create the parent directory if needed, merge the selected facts into the existing Markdown profile, preserve unrelated entries, and read it back before confirming what was saved. Honor requests to inspect, correct, or forget entries. If the user declines, continue giving advice without a write. If the client cannot access persistent local storage, explain that the advice applies to this chat and offer a short summary the user can reuse. Never report a successful save without checking it.
