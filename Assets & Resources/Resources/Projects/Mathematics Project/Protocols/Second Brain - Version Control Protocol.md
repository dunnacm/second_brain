---
type: protocol
project: second_brain
status: current
---

# Second Brain - Version Control Protocol

## Summary for the user

**second_brain is both your Obsidian vault and your local Git repository.** Git records selected changes as local commits. GitHub holds the remote copy after those commits are pushed. Saving an Obsidian note, committing it, and pushing it are three separate steps.

Use **GitHub Desktop on Windows** for a visual review, or ask the assistant to perform the same workflow with Git. Ubuntu through WSL is another command-line environment; it is not another GitHub repository.

The usual goal is to preserve the intended vault changes on **main**, with a descriptive commit and a verified push. A request to rename notes or write this protocol does not itself request a commit or push.

This document currently lives in **Assets & Resources → Resources → Projects → Mathematics Project → Protocols**. It applies to version control for the whole vault.

## Confirmed repository identity

Verified from local Git on **2026-09-16**:

| Item | Value |
| --- | --- |
| Local repository and vault root | `C:\Users\dunnc\My Drive (cardonadunn@gmail.com)\PRESENT\Η βιβλιοθήκη\second_brain` |
| Git history and configuration | The `.git` directory inside that root |
| Configured GitHub remote | [dunnacm/second_brain](https://github.com/dunnacm/second_brain) |
| Remote name | `origin` |
| Current branch | `main` |
| Upstream branch | `origin/main` |
| Most recent local commit at inspection | `c5608fe` — Save vault changes for 2026-03-27 |

The Windows folder is the **local repository**; GitHub is its **remote repository**. The remote address and tracking branch were verified locally. No network fetch or push was performed while creating this document, so this snapshot does not establish whether GitHub currently matches the local files.

## What has happened in this project

Earlier project sessions saved vault changes to GitHub and brought the work onto main. The repository state recorded on September 16 ended at the March 27 commit listed above. Later changes must be checked against fresh Git output.

An earlier broad reorganization was reverted at the user's request. At the September 16 inspection, the top-level folder was **Systems and Resources**. The current vault has since been reorganized under **Assets & Resources** and **Lexicon**. The September 16 pass relabeled Mathematics Project support material, added concise Properties, and created this protocol.

The Mathematics Project notes now use three plain-text Properties: **type**, **project**, and **status**. There are no links in those Properties. Version numbers and snapshot dates remain in filenames. Protocol v07 is labeled current because it is the version outside Archive; its content has not been reconciled into a new specification. The nested-list MOC experiments remain draft because the source contains repeated blocks and an incomplete closing fence.

## User workflow with GitHub Desktop

1. Save your Obsidian work. Select **second_brain** in GitHub Desktop. If it is not listed, use **File → Add local repository** and select the confirmed vault root. Add the existing repository. [GitHub Desktop instructions](https://docs.github.com/en/desktop/adding-and-cloning-repositories/adding-a-repository-from-your-local-computer-to-github-desktop).
2. Confirm that **Current Branch** is **main**. Click **Fetch origin** to check for remote commits. If the remote has changes, preserve local work before pulling. If Desktop reports a conflict, resolve it before continuing. [Synchronization instructions](https://docs.github.com/en/desktop/working-with-your-remote-repository-on-github-or-github-enterprise/syncing-your-branch-in-github-desktop).
3. Review the **Changes** list and select the files for this save. Inspect deletions and renamed files. Write a descriptive summary, then **Commit to main**. For this task, a suitable summary would be: “Label mathematics resources and document the version-control workflow.” [Review and commit instructions](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop).
4. Click **Push origin**. Confirm it succeeds and that no further outgoing commits remain. A local commit alone does not update GitHub. [Push instructions](https://docs.github.com/en/desktop/making-changes-in-a-branch/pushing-changes-to-github-from-github-desktop).

If you only want to save selected notes, select those files. If you want to save the whole vault, review the entire change list, including the Obsidian settings and plugins that Git already tracks.

## Example prompt to update the repository

Copy this into a chat when you want a complete repository update:

```text
Please save the intended current changes in my second_brain vault to GitHub.

Local repository:
C:\Users\dunnc\My Drive (cardonadunn@gmail.com)\PRESENT\Η βιβλιοθήκη\second_brain

Read:
Assets & Resources/Resources/Projects/Mathematics Project/Protocols/Second Brain - Version Control Protocol.md

Expected remote: https://github.com/dunnacm/second_brain.git
Target branch: main

Review the full working tree, including additions, deletions, renames,
and tracked Obsidian settings/plugin changes. Preserve my current files.
Respect .gitignore and exclude credentials and machine-local artifacts.

Fetch the remote state, preserve local work, and reconcile incoming
changes safely. Commit the intended vault updates with descriptive
messages and push to origin/main. This request authorizes that commit
and push; do not stop merely to ask again.

If a conflict or ambiguous deletion requires my judgment, explain the
specific choice and give me one next action. Do not discard work,
force-push, or rewrite published history.

Finish by reporting the commit ID(s), the push result, any changes left
uncommitted, and whether main matches the remote after verification.
Update the session record in the protocol with the actual outcome.
```

For a smaller save, replace “full working tree” with the specific folders or files you want included.

## Instructions for the AI assistant

### Establish the actual state

1. Read this document and the user's current request. Locate applicable local instructions. Treat this page as continuity information, not permission to publish without an update request.
2. Confirm the repository root, current branch, remote address, upstream, current commit, working-tree changes, and staged changes. Do not initialize a new repository inside a project subfolder.
3. Preserve the user's existing edits and staged work. Distinguish new work from pre-existing changes. Current files and fresh Git output take precedence over historical chat summaries.
4. Default to the user's established main-branch workflow when that is the requested target. If the checkout is on another branch, inspect its history and changes before deciding how to bring the intended work onto main.

Useful inspection commands, run from the verified root:

```shell
git rev-parse --show-toplevel
git branch --show-current
git remote -v
git status --short --branch
git diff --stat
git diff --cached --stat
git log -1 --oneline
```

### Carry out an authorized save

1. Review the actual diff, untracked files, and deletions. A folder rename may appear as removed old paths and added new paths before staging. Verify content and destinations rather than treating every deletion as lost data.
2. Review the existing ignore rules. This vault ignores tokens, workspace state, sync-conflict copies, and certain device/backup files. Many other .obsidian files are already tracked. Do not exclude or stage the whole directory blindly. A new ignore rule does not remove an already tracked secret from history.
3. Fetch origin and compare main with origin/main. A fetch refreshes remote-tracking information; it does not merge remote content into the working files. [Git fetch reference](https://git-scm.com/docs/git-fetch).
4. Preserve local work before integrating incoming changes. If only behind, use a fast-forward when the working state permits it. If both sides have commits, inspect the divergence and use a non-destructive merge consistent with the request. Resolve routine conflicts only when the intended content is clear; ask the user about substantive ambiguity. Do not reset, clean, discard, or force-push to make synchronization easier.
5. Stage the reviewed scope, inspect the staged diff, and create descriptive commits. If everything is already committed, do not create an empty commit. If committed work is merely unpushed, push that work.
6. Push to the verified remote and branch. Check the result and refresh/verify the remote branch ID against local HEAD. Report rejected pushes, authentication failures, remaining local changes, or unavailable network access accurately. [Git push reference](https://git-scm.com/docs/git-push).
7. Record the actual outcome below. When a commit is still being prepared, label the record accordingly. If recording the final commit ID afterward leaves this protocol modified, report that explicitly; do not claim a clean working tree. Do not create an endless chain of commits merely to embed each commit's own ID.

### Use Windows and WSL deliberately

This vault currently lives on the Windows filesystem and is used by Windows Obsidian. Prefer Windows Git/GitHub Desktop for routine saves here. Use one Git client at a time for changes to this checkout; do not run Desktop and WSL Git operations concurrently.

With WSL's usual C-drive mount, the same folder is:

```text
/mnt/c/Users/dunnc/My Drive (cardonadunn@gmail.com)/PRESENT/Η βιβλιοθήκη/second_brain
```

In Ubuntu, quote the path because it contains spaces and parentheses:

```bash
cd '/mnt/c/Users/dunnc/My Drive (cardonadunn@gmail.com)/PRESENT/Η βιβλιοθήκη/second_brain'
git rev-parse --show-toplevel
git status --short --branch
```

This is an expected path under the standard WSL mount configuration, not a verified Ubuntu installation in this session. Verify it before use. Windows Git and WSL Git may have different configuration and credentials. Check line-ending settings if switching clients causes widespread formatting-only changes; do not mass-convert the vault or change global Git settings as an incidental fix. [Microsoft's Git-on-WSL guidance](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git).

The repository is also inside a Google Drive folder. File synchronization is separate from Git commits and pushes. If sync-conflict copies or repository lock problems appear, stop overlapping writers, preserve the files, and diagnose the specific problem before retrying.

## Carrying this project into another chat or project

A future assistant may not see this conversation. Give it this document or its current path, the actual repository location, and the requested next action.

Use this handoff prompt:

```text
Continue version-control maintenance for my second_brain Obsidian vault.

Read:
Assets & Resources/Resources/Projects/Mathematics Project/Protocols/Second Brain - Version Control Protocol.md

Repository root:
C:\Users\dunnc\My Drive (cardonadunn@gmail.com)\PRESENT\Η βιβλιοθήκη\second_brain

Verify the current root, remote, branch, staged changes, and working tree.
Use the latest user request and current files as the source of truth.
Do not assume that an old chat's “pushed” or “clean” status is still true.

My next requested action:
[State the task, and whether you want a local edit, commit, or commit-and-push.]

Work one requested step at a time and preserve unrelated work.
```

If moving to another machine or a genuinely different repository, establish the new root and remote explicitly. For an existing checkout, open that checkout. For a fresh machine, clone the intended remote once and verify its destination. Carry over the workflow, relevant notes, and any uncommitted changes separately; uncommitted work is not included in a GitHub clone.

## Latest session record

**Date:** 2026-09-27.
**Completed:** fetched `origin/main`, reviewed the vault reorganization and Obsidian plugin changes, updated the repository guide and ignore rules, and prepared the intended changes for a commit on `main`.
**Preserved:** 86 locally absent notes remain in GitHub's history and current branch, including 75 inventory notes, pending mathematics notes, language and graph notes. Their local deletions remain unstaged because their removal was not established as intentional. Generated plugin backups, test state, and Python bytecode remain local and ignored.
**Repository state:** `main` and `origin/main` matched at `c5608fe` before this update. A stale Git lock from September 16 was removed after confirming no Git process was running.
**Publication status:** committed and pushed the reviewed changes to `origin/main`; use Git log for the final commit ID and verify the local and remote branch IDs after any future update.
**Next action:** decide whether to restore the 86 absent notes locally or record their deletion in a later commit.

### Previous session: 2026-09-16

**Completed:** relabeled the Mathematics Project support folders and 14 notes; added three plain-text Properties to each; created this version-control protocol under Projects.
**Preserved:** original note bodies, mathematical formatting, the existing Archive arrangement, and unrelated vault work. Existing path references were updated where needed.
**Repository state:** main tracking origin/main; substantial pre-existing local changes; HEAD observed as c5608fe.
**Publication status:** local edits only; no fetch, commit, or push performed for that task.
**Next action:** review the labels and protocol; request a repository update when ready.
