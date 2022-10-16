#!/usr/bin/bash
tag_list=$(pip install --trusted-host pypi.home -i http://"$PYPI_USER":"$PYPI_PASSWORD"@pypi.home horizons_client==version 2>&1)
if [[ ${tag_list} == *"$(poetry version -s)"* ]]; then
    echo "Bumping Horizons API version"
    poetry version patch
    exit 1
else
    echo "Horizons API version ok"
    exit 0
fi
