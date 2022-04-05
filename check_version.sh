#!/usr/bin/bash
tag_list=$(poetry add horizons_client@latest --dry-run)
if [[ ${tag_list} == *"$(poetry version -s)"* ]]; then
    echo "Bumping Horizons API version"
    poetry version patch
    exit 1
else
    echo "Horizons API version ok"
fi
