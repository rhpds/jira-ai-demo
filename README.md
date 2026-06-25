# Jira AI Integration Demo

This is a demo repository showing how to use the RHPDS reusable Jira AI workflow with PR templates.

## How it works

1. Create a PR with the PR template (auto-filled by GitHub)
2. Fill in the Jira ticket number in the template: `**Jira:** RHCLOUD-1234`
3. GitHub Actions automatically:
   - Validates that a Jira ticket is present
   - Gets the PR diff
   - Analyzes it with Claude AI
   - Posts a summary to the Jira ticket

## Testing the workflow

1. Create a branch and make changes:
   ```bash
   git checkout -b feature/improve-validation
   # Edit app.py
   git add app.py
   git commit -m "Improve password validation"
   git push origin feature/improve-validation
   ```

2. Create a PR (the template will auto-fill):
   ```bash
   gh pr create --fill
   ```

3. Edit the PR description to add your Jira ticket:
   ```markdown
   **Jira:** RHCLOUD-1234
   ```

4. Check the Actions tab to see the workflow run

5. Check Jira ticket RHCLOUD-1234 for the AI-generated comment

## PR Template

The `.github/pull_request_template.md` file is automatically used by GitHub for all PRs.

## Workflow files

- `.github/workflows/jira-update.yml` - Calls the reusable workflows
- Validation and AI analysis are in the central `rhpds-workflows` repo

## Different tickets per PR

Each PR can reference a different Jira ticket - just update the `**Jira:**` field in the PR description.
