# Personal LeetCode MCP server

Tools: `get_problem(number)`, `get_my_solution(number, lang=None)`.

Setup (uses [uv](https://docs.astral.sh/uv/)):
```
cd tools/leetcode-mcp
uv sync
```
MCP config: `command: "uv"`, `args: ["run", "--directory", "<abs path to tools/leetcode-mcp>", "leetcode_mcp.py"]`.

Cookies (`LEETCODE_SESSION`, `LEETCODE_CSRF`) go ONLY in the MCP config env, never in this repo.
