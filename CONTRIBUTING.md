# Contributing to homebrew-grazer

Thanks for helping maintain the Grazer Homebrew tap. This repository packages
the `grazer` formula used to install the Grazer skill and its Python resources
through Homebrew.

## Good First Contributions

- Update the formula when a new `grazer-skill` release is available.
- Fix formula metadata, caveats, or documentation links.
- Improve comments or contributor documentation.
- Refresh Python resource versions and checksums when dependencies change.
- Report install or test results from macOS and Homebrew environments.

## Before You Open a Pull Request

1. Check existing issues and pull requests to avoid duplicate formula updates.
2. Keep each pull request focused on one formula or documentation change.
3. Use clear commit messages, such as `formula: update grazer to 1.3.1`.
4. Do not commit local Homebrew cache files, bottles, logs, credentials, or
   generated archives.
5. Include the Homebrew commands you ran, or explain why the change is
   documentation-only.

## Formula Guidelines

- Keep the formula class name and filename aligned with Homebrew conventions.
- Update `url`, `sha256`, and any Python `resource` blocks together.
- Prefer upstream release artifacts from PyPI or the canonical project source.
- Keep caveats concise and focused on commands users can run after install.
- Do not change license metadata unless the upstream project license changed.

## Validation

Run the most relevant checks for the change:

```bash
brew audit --strict --online Formula/grazer.rb
brew style Formula/grazer.rb
brew test grazer
```

If a check cannot be run locally, note the reason in the pull request.

## Pull Request Checklist

- [ ] The change is scoped to the Grazer Homebrew tap.
- [ ] Formula URLs and checksums were checked.
- [ ] Homebrew audit, style, or test results are included when relevant.
- [ ] No generated artifacts or local machine-specific files were added.

## Review Process

Maintainers may ask for a narrower diff, updated checksums, or clearer test
notes before merging. That keeps the tap easy to review and reliable for
Homebrew users.
