#!/bin/sh

ROOT_DIR=`dirname "$0"`

# remove migrations
find "$ROOT_DIR" -name "migrations" -type d | xargs -n 1 -J "%" find % -type f -name "[0-9]*.py" -exec rm {} +

# remove __pycache__
find "$ROOT_DIR" -iname "__pycache__" -exec rm -rf {} +

# remove logs
rm -r "$ROOT_DIR/logs"
