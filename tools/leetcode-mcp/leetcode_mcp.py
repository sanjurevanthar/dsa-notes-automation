"""
Personal LeetCode MCP server.
Two tools: get_problem(number) and get_my_solution(number, lang=None).

Setup:
  pip install "mcp[cli]" httpx
Env vars (set in Claude Desktop config, never commit them):
  LEETCODE_SESSION  - your LEETCODE_SESSION cookie
  LEETCODE_CSRF     - your csrftoken cookie
"""
import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE = "https://leetcode.com"
SESSION = os.environ.get("LEETCODE_SESSION", "")
CSRF = os.environ.get("LEETCODE_CSRF", "")

HEADERS = {
    "Content-Type": "application/json",
    "Referer": BASE,
    "User-Agent": "Mozilla/5.0",
    "x-csrftoken": CSRF,
    "Cookie": f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF}",
}

mcp = FastMCP("my-leetcode")
_slug_cache: dict[int, dict] = {}


def _gql(query: str, variables: dict) -> dict:
    r = httpx.post(f"{BASE}/graphql/", json={"query": query, "variables": variables},
                   headers=HEADERS, timeout=30)
    r.raise_for_status()
    data = r.json()
    if data.get("errors"):
        raise RuntimeError(data["errors"])
    return data["data"]


def _lookup(number: int) -> dict:
    """Problem number -> {slug, title, difficulty}. Cached after first call."""
    if not _slug_cache:
        r = httpx.get(f"{BASE}/api/problems/all/", headers=HEADERS, timeout=30)
        r.raise_for_status()
        levels = {1: "Easy", 2: "Medium", 3: "Hard"}
        for p in r.json()["stat_status_pairs"]:
            s = p["stat"]
            _slug_cache[int(s["frontend_question_id"])] = {
                "slug": s["question__title_slug"],
                "title": s["question__title"],
                "difficulty": levels.get(p["difficulty"]["level"], "?"),
            }
    if number not in _slug_cache:
        raise ValueError(f"Problem {number} not found")
    return _slug_cache[number]


@mcp.tool()
def get_problem(number: int) -> dict:
    """Get a LeetCode problem's title, slug, difficulty, topic tags and description (HTML) by problem number."""
    info = _lookup(number)
    q = _gql("""
      query q($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
          questionFrontendId title titleSlug difficulty content
          topicTags { name }
        }
      }""", {"titleSlug": info["slug"]})["question"]
    q["topicTags"] = [t["name"] for t in q["topicTags"]]
    q["url"] = f"{BASE}/problems/{info['slug']}/"
    return q


@mcp.tool()
def get_my_solution(number: int, lang: str | None = None) -> dict:
    """Get MY most recent Accepted submission (code, language, runtime/memory percentile) for a problem number.
    Optional lang filter, e.g. 'cpp', 'python3', 'java'."""
    info = _lookup(number)
    subs = _gql("""
      query s($offset: Int!, $limit: Int!, $questionSlug: String!) {
        questionSubmissionList(offset: $offset, limit: $limit, questionSlug: $questionSlug) {
          submissions { id statusDisplay lang timestamp }
        }
      }""", {"offset": 0, "limit": 40, "questionSlug": info["slug"]})
    accepted = [s for s in subs["questionSubmissionList"]["submissions"]
                if s["statusDisplay"] == "Accepted" and (lang is None or s["lang"] == lang)]
    if not accepted:
        return {"number": number, "title": info["title"], "found": False,
                "message": "No accepted submission found (check cookie or lang filter)."}
    latest = max(accepted, key=lambda s: int(s["timestamp"]))
    d = _gql("""
      query d($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
          code runtimeDisplay runtimePercentile memoryDisplay memoryPercentile timestamp
          lang { name verboseName }
        }
      }""", {"submissionId": int(latest["id"])})["submissionDetails"]
    return {
        "number": number, "title": info["title"], "slug": info["slug"],
        "difficulty": info["difficulty"], "found": True,
        "lang": d["lang"]["name"], "code": d["code"],
        "runtime": d["runtimeDisplay"], "runtime_beats": d["runtimePercentile"],
        "memory": d["memoryDisplay"], "memory_beats": d["memoryPercentile"],
    }


if __name__ == "__main__":
    mcp.run()
