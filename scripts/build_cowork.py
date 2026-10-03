"""Build dist/mizan.plugin for the Claude app (Cowork).

Same skills as the Claude Code plugin, with two changes: the MCP server URL is fixed (no
userConfig prompt for the user to fill in), and userConfig is dropped from the manifest.

    python scripts/build_cowork.py [--url https://mizan.example.com]
"""

import argparse
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "plugins" / "mizan"
DIST = ROOT / "dist"
DEFAULT_URL = "https://mizan.141-94-76-77.sslip.io"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=DEFAULT_URL, help="Mizan address, no trailing slash")
    url = parser.parse_args().url.rstrip("/")

    manifest = json.loads((SRC / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    manifest.pop("userConfig", None)
    manifest["description"] = manifest["description"].replace("Claude Code", "Claude")

    mcp = json.loads((SRC / ".mcp.json").read_text(encoding="utf-8"))
    mcp["mcpServers"]["mizan"]["url"] = f"{url}/mcp"

    DIST.mkdir(exist_ok=True)
    out = DIST / "mizan.plugin"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(".claude-plugin/plugin.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
        z.writestr(".mcp.json", json.dumps(mcp, indent=2) + "\n")
        for path in sorted(SRC.rglob("*")):
            rel = path.relative_to(SRC).as_posix()
            if path.is_file() and rel not in (".claude-plugin/plugin.json", ".mcp.json"):
                z.write(path, rel)
    print(f"{out} ({manifest['version']}, {url}/mcp)")


if __name__ == "__main__":
    main()
