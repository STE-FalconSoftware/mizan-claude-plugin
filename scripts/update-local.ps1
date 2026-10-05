# Bring this PC's Claude Code up to the plugin version in this folder, and rebuild the Cowork file.
#
#   powershell -ExecutionPolicy Bypass -File scripts\update-local.ps1
#
# Then restart Claude Code (or /reload-plugins). For Cowork, upload dist\mizan.plugin again.
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot

claude plugin marketplace update mizan
claude plugin update mizan@mizan
# Project-scoped installs (e.g. a test folder) are updated too; missing ones are skipped.
$installed = Get-Content "$env:USERPROFILE\.claude\plugins\installed_plugins.json" -Raw | ConvertFrom-Json
foreach ($entry in $installed.plugins.'mizan@mizan') {
    if ($entry.scope -eq "project" -and (Test-Path $entry.projectPath)) {
        Push-Location $entry.projectPath
        try { claude plugin update mizan@mizan --scope project } finally { Pop-Location }
    }
}

python "$root\scripts\build_cowork.py"
Write-Host "Done. Restart Claude Code; for Cowork upload $root\dist\mizan.plugin."
