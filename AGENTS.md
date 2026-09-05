# Local Windows installation
- Purpose: independent upstream AI video automation project; see README for capabilities.
- Fork: https://github.com/drairelax-ctrl/yt-automation
- Upstream: https://github.com/mzu-2410z/yt-automation
- Start: run.bat from any working directory. Setup: setup.bat.
- Python environment: .venv (Viral uses Docker / trendscraper/src/node_modules).
- Settings and credentials: .env; MoneyPrinterTurbo also uses ignored config.toml; YT OAuth uses ignored client_secrets.json and youtube_token.pkl.
- Local additions: setup.bat, run*.bat, windows_*.py/js and this file. Compare with upstream using git diff; never overwrite existing work.
- Do not commit secrets, environments, caches, downloaded models, or generated media. Never run paid generation or upload without the user's authorization.
- No project integration, reset, force push, branch deletion, or automatic commit/push.
