#!/bin/sh
# Builds dist/jashn-e-yaarana-site.zip: only the finished website (html, css, js, images).
# index.html sits at the root of the zip. No scripts or build folders are included.
set -e
cd "$(dirname "$0")"
python3 build.py
mkdir -p dist
rm -f dist/jashn-e-yaarana-site.zip
(cd site && zip -r -q -X ../dist/jashn-e-yaarana-site.zip . -x '.DS_Store' -x '*/.DS_Store')
echo "Built dist/jashn-e-yaarana-site.zip"
unzip -l dist/jashn-e-yaarana-site.zip | tail -1
