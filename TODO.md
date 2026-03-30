# Deployment TODO - GovData Insight to Heroku

## Approved Plan Steps

### 1. Prepare Git Repo (Pending)
- `git add .`
- `git commit -m "Prepare for Heroku deployment"`

### 2. Install Heroku CLI (Pending)
- Download from https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli
- Run installer
- `heroku login`

### 3. Create & Deploy (Pending)
- `heroku create govdata-insight-[unique]`
- `git push heroku main`
- `heroku open`

### 4. Verify (Pending)
- `heroku logs --tail`
- `heroku ps:scale web=1`

**Status: Ready to execute step-by-step. Mark as [DONE] when completed.**

