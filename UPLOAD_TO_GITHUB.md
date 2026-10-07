# Upload To GitHub

Suggested repository name: `lou-thomas-physics`

Suggested description: `Lou Thomas's exploratory physics research in cosmology, relational substrates, and quantum foundations, with manuscripts, code, data, and reproducibility checks.`

This folder is the upload package. Do not upload the parent Hub, the task's working directory, source-drive backups, or a pre-existing Git history. No remote repository has been created and nothing has been pushed for you.

## Prepared Local Repository

When this folder is already listed in GitHub Desktop on `main` with "No local changes", the initial commit is already prepared. Use **Publish repository**; do not initialize another repository or create an empty commit. The bottom-left Summary and Description fields describe a commit. The Publish dialog's Description describes the repository.

Initial commit summary:

```text
Initial release of Lou Thomas's physics research
```

Initial commit description:

```text
Consolidates BIH-VI cosmology, RNSF lattice models, and quantum-foundation studies into one research archive. Includes manuscripts, numerical code, data, figures, reproducibility checks, citation guidance, and documented limitations. Personal, AI-assisted exploratory research; not peer-reviewed.
```

The instructions below are for initializing a fresh archive copy, not for repeating setup in an already prepared repository.

## Before The First Commit

Use your personal GitHub account. In GitHub's email settings, copy your actual GitHub-provided no-reply commit email. In GitHub Desktop's Git settings, use **Lou Thomas** and that no-reply address, not an employer email. Check the identity before committing: Git history can retain an email even after you remove it from a document.

Review [OPEN_DECISIONS.md](OPEN_DECISIONS.md). In particular, confirm that you have the right to release the included work. A privacy scan and a personal-research disclaimer cannot determine employment agreements, patent consequences, or third-party rights. No blanket legal protection is promised here.

## GitHub Desktop

1. Extract the ZIP, or use the supplied folder as-is. Open a terminal **in that folder** and run `git init -b main`. This creates only a local repository.
2. In GitHub Desktop, choose **File > Add local repository** and select this folder.
3. Inspect Changes. Include the documents, code, results, and hidden `.gitignore`/`.gitattributes` files. Do not include `_generated/`, environments, secrets, or unrelated work.
4. Commit with a message such as `Initial consolidated research release 2026.10.07`.
5. Select **Publish repository**. Start with **Keep this code private** checked and the owner set to your personal account. Review the rendered README, citation button, files, and commit identity online.
6. When you have finished that review and accepted the licensing/rights decisions, change visibility to public in GitHub's repository settings. Public copies and forks cannot reliably be recalled.

Do not upload the ZIP as the only repository file: GitHub should show `README.md`, `CITATION.cff`, and the research folders at the root. The ZIP can later be attached to a GitHub release as a convenience copy.

## Optional Command Line

From this folder, initialize locally and set identity **for this repository only**:

```powershell
git init -b main
git config --local user.name "Lou Thomas"
git config --local user.email "REPLACE_WITH_YOUR_ACTUAL_GITHUB_NOREPLY_EMAIL"
git config --local --get user.email
python tools/verify_release.py
git add .
git status --short
git diff --cached --stat
git commit -m "Initial consolidated research release 2026.10.07"
```

Replace the email placeholder before running the commit. Then create an empty private repository on GitHub, without adding another README or license, and follow GitHub's displayed commands to connect and push this local repository. No credentials belong in a remote URL or in these files.

## Citation And A Stable Release

`CITATION.cff` already identifies Lou Thomas and this edition. It deliberately contains no invented repository URL, DOI, ORCID, or publication date. After the real repository URL is known, add it to the citation file and citation guide. A tagged release can later be archived through a DOI service; that is a separate action, not something this local package has done.

If you edit any distributed file, the current checksums should fail. That is expected: issue a new version and regenerate its manifest/checksums after review instead of claiming the original seal still matches.

References: [GitHub Desktop: adding a local repository](https://docs.github.com/en/desktop/adding-and-cloning-repositories/adding-a-repository-from-your-local-computer-to-github-desktop), [GitHub citation files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files), [commit email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).
