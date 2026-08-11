# Forgejo workflow stubs

**These are live.** LenoreCraft cut over during Phase 6: the forge
(`lenore/LenoreCraft`) is the writer, and GitHub is a push mirror kept for the
public face and offsite DR.

All the real logic lives once in `lenore/lenore-ci`, pinned at `@v1` — a moving
major tag, following the actions convention. A fix there reaches every repo
without an edit here.

| Stub | Calls | Fires on |
|---|---|---|
| `release.yml` | `release.yml@v1` | push to `main`/`rc`/`beta`/`alpha` |
| `build-publish.yml` | `build-publish.yml@v1` | `release: published`, or dispatch by tag |
| `docs.yml` | `docs.yml@v1` (`mode: preview`) | push to `main` |
| `docs-release.yml` | `docs.yml@v1` (`mode: release`) | `release: published`, or dispatch by tag |
| `announce.yml` | `announce.yml@v1` (`target: reddit`) | `release: published`, or dispatch by tag |
| `pr-title-lint.yml` | `pr-title-lint.yml@v1` | `pull_request` |

There is no `tests.yml` stub — this repo has no test suite. Add one when it does.

## What this replaced, and why it was a rework rather than a port

LenoreCraft was the last repo in the fleet with **no semantic-release at all**.
Versioning was `scripts/versioning.sh`: it read `scripts/version.txt`, looked
for `[major]` or `[minor]` in the commit subject, incremented, then committed
and pushed the bump itself. Publishing was gated on the word `publish` appearing
somewhere in a commit message, and the whole chain hung off a `workflow_run`
that fired when the docs deploy finished.

Three consequences, all now gone:

* **The version depended on prose.** A release could be missed by forgetting a
  keyword, or cut twice by a rebase that reused a subject line.
* **Only `main` and `beta` existed**, so there was no rc/alpha channel model and
  no `refs/notes/semantic-release` — the ref every other repo's mirror is
  configured to protect. `rc` and `alpha` were created at cutover and the notes
  ref was seeded at `v0.0.12` so the counter continues rather than restarting.
* **`docker.yml` published `:latest` unconditionally**, with no check that the
  tag being built was actually the newest. That is the bug that made LenoreShop
  serve 1.7 as `latest` for 72 days; `build-publish` compares aliases by digest
  and refuses to move one backwards.

## 🔴 `.github/workflows/` is gone, and it must stay gone

Forgejo reads **both** `.github/workflows/` and `.forgejo/workflows/`. With
Actions enabled on the forge, restoring that directory means every workflow runs
twice — and two `semantic-release` instances on one push is the double-bump
anomaly this migration exists to prevent.

## 🔴 Never merge on GitHub

GitHub is a **push mirror**, so a merge performed there is not a contribution —
it is a divergence. A `non_fast_forward` ruleset guards `main`/`rc`/`beta`/
`alpha` there, which converts that mistake from silent data loss into a loud,
detectable mirror failure. Land the work on the forge and let the mirror carry
it back. Issues stay on GitHub permanently; the forge's tracker is disabled.
