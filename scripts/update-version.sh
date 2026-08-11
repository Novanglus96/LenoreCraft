#!/bin/bash
# Usage: ./scripts/update-version.sh <version>
# Updates version references across the project for a semantic-release prepare step.
#
# Replaces scripts/versioning.sh and scripts/ver_change.sh, which decided the
# NEXT version themselves — versioning.sh read scripts/version.txt, looked for
# [major]/[minor] in the commit subject, incremented, and then committed and
# pushed the result. semantic-release owns all of that now: the version comes
# from the conventional-commit history, and @semantic-release/git makes the
# commit. This script only writes the number it is handed.
#
# 🔴 Every path below must exist. `sed` on a missing file prints an error and
# carries on, and a script that ends in an `echo` still exits 0 — so a stale
# path means a version reference silently stops being updated while the release
# reports success. The guard makes that loud.

VERSION=$1
if [ -z "$VERSION" ]; then
  echo "Usage: $0 <version>"
  exit 1
fi

VERSION_FILE="scripts/version.txt"
BACKEND_DOCKER_FILE="backend/Dockerfile"
FRONTEND_DOCKER_FILE="frontend/Dockerfile"
MODEL_VERSION_FILE="backend/administration/fixtures/version.json"
API_PY_FILE="backend/backend/urls.py"
PACKAGE_JSON_FILE="frontend/package.json"
APPNAVIGATION_VUE_FILE="frontend/src/views/AppNavigationVue.vue"
APP_VUE_FILE="frontend/src/App.vue"

missing=0
for f in "$BACKEND_DOCKER_FILE" "$FRONTEND_DOCKER_FILE" "$MODEL_VERSION_FILE" \
         "$API_PY_FILE" "$PACKAGE_JSON_FILE" "$APPNAVIGATION_VUE_FILE" "$APP_VUE_FILE"; do
  if [ ! -f "$f" ]; then
    echo "ERROR: $f does not exist — update-version.sh is out of date with the repo"
    missing=1
  fi
done
[ "$missing" -eq 1 ] && exit 1

echo "$VERSION" > "$VERSION_FILE"
sed -i -r "s/^LABEL version=\"[^\"]*\"/LABEL version=\"$VERSION\"/" "$BACKEND_DOCKER_FILE"
sed -i -r "s/^LABEL version=\"[^\"]*\"/LABEL version=\"$VERSION\"/" "$FRONTEND_DOCKER_FILE"
sed -i -r "s/\"version_number\": \"[^\"]*\"/\"version_number\": \"$VERSION\"/" "$MODEL_VERSION_FILE"
sed -i -r "s/^api.version = \"[^\"]*\"/api.version = \"$VERSION\"/" "$API_PY_FILE"
sed -i -r "s/\"version\": \"[^\"]*\"/\"version\": \"$VERSION\"/" "$PACKAGE_JSON_FILE"
sed -i -r "s/(<span[^>]*>v)[0-9]+(\.[0-9]+)*(<\/span>)/\1$VERSION\3/" "$APPNAVIGATION_VUE_FILE"
sed -i -r "s/\"[0-9]+\.[0-9]+\.[0-9]{1,3}\"/\"$VERSION\"/" "$APP_VUE_FILE"

echo "Updated version to $VERSION"
