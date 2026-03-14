import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

USERNAME = os.getenv("GITHUB_USERNAME")
url = f"https://api.github.com/users/{USERNAME}/repos?per_page=20&sort=pushed"

response = requests.get(url)
repos = response.json()

now = datetime.now(timezone.utc)

print(f"\n{'REPO':<35} {'LAST PUSH':<15} STATUS\n" + "-" * 60)

for repo in repos:
      name = repo["name"]
      pushed = datetime.fromisoformat(repo["pushed_at"].replace("Z", "+00:00"))
      days_ago = (now - pushed).days

      if days_ago <= 30:
          status = "🟢 ACTIVE"
      elif days_ago <= 180:
          status = "🔴 STALE"
      else:
          status = "⚪ INACTIVE"

      print(f"{name:<35} {days_ago:<15} {status}")

print()

