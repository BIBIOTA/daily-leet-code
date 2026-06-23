# Daily LeetCode

> **Primary language: Traditional Chinese (繁體中文)** — all responses, explanations, and hints must be in Traditional Chinese.

Personal daily LeetCode practice repo, powered by the [`leetcode-skill`](https://github.com/BIBIOTA/yuki-marketplace/tree/master/plugins/leetcode-skill) plugin for guided problem-solving, session tracking, and weak-area analysis.

---

## Agents

[AGENTS.md](./AGENTS.md)

---

## Plugin: leetcode-skill

Source: [BIBIOTA/yuki-marketplace — plugins/leetcode-skill](https://github.com/BIBIOTA/yuki-marketplace/tree/master/plugins/leetcode-skill)

### Available Commands

| Command | Skill | Description |
|---------|-------|-------------|
| `/leetcode <url>` | `leetcode-skill:leetcode` | Start a practice session: fetch the problem, create a solution stub, initialise session state |
| `/leetcode --next` or `/next` | `leetcode-skill:leetcode-next` | Recommend the next problem based on weak-area data, then hand off to `/leetcode <url>` |
| `/leetcode --profile` | `leetcode-skill:leetcode` | View progress dashboard or edit settings |
| `/leetcode --review` | `leetcode-skill:leetcode` | Re-attempt a previously struggled problem |
| `/hint` | `leetcode-skill:leetcode-hint` | Deliver the next progressive hint (5 rungs, never skips) |
| `/run` | `leetcode-skill:leetcode-run` | Run the current solution against examples + edge cases, report pass/fail |
| `/submit` | `leetcode-skill:leetcode-submit` | Full evaluation: correctness, time complexity, space complexity, code quality |
| `/finish` | `leetcode-skill:leetcode-finish` | End the session: write to log, update weak-area tracking, clear session state |

### Hint Ladder

`/hint` advances exactly one rung per call — never skips:

1. **Rung 1 — Reframe**: Restate what the problem is really asking; no pattern name yet
2. **Rung 2 — Pattern category**: Name the general technique (e.g. two pointers, sliding window)
3. **Rung 3 — Structural hint**: Describe the shape of the solution — what state to track, loop invariant
4. **Rung 4 — Pseudocode**: Provide pseudocode or a heavily-commented skeleton
5. **Rung 5 — Worked example**: Step-by-step trace on the example input (only if still stuck after Rung 4 and user explicitly asks again)

---

## Directory Structure

```
.leetcode/
├── notes/
│   └── heap-counter.md          # Pattern notes / cheat sheets
└── performance/
    ├── log.md                    # Practice log (date, problem, pattern, result, hints used)
    ├── session-state.md          # Active session state (slug, hint rung, status)
    └── weak-areas.md             # Weak-area tracking (struggle rate by pattern)

solutions/                        # Solution files (default: Python)
```

---

## Language Settings

- Default solution language: Python
- To change, update `.leetcode/user-profile.md` via `/leetcode --profile`

---

## Copyright Notice

LeetCode problem text is copyrighted. The skill always **paraphrases** problem descriptions — it never reproduces original text verbatim.
