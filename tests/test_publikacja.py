"""Spójność metadanych publikacji: server.json (MCP Registry), pyproject.toml i README."""

import json
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
server = json.loads((ROOT / "server.json").read_text(encoding="utf-8"))
project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]


def test_server_json_basics():
    assert server["name"] == "io.github.tmierzwa/fikus"
    assert re.fullmatch(r"[a-zA-Z0-9.-]+/[a-zA-Z0-9._-]+", server["name"])
    assert 1 <= len(server["description"]) <= 100
    assert server["repository"] == {"url": "https://github.com/tmierzwa/fikus", "source": "github"}
    (pkg,) = server["packages"]
    assert pkg["registryType"] == "pypi"
    assert pkg["identifier"] == project["name"]
    assert pkg["transport"] == {"type": "stdio"}


def test_versions_match_pyproject():
    assert server["version"] == project["version"]
    assert all(p["version"] == project["version"] for p in server["packages"])


def test_readme_has_mcp_name():
    # MCP Registry sprawdza własność paczki PyPI po tej linii w opisie paczki (README).
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert f"<!-- mcp-name: {server['name']} -->" in readme
