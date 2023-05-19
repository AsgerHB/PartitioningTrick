#!/usr/bin/env bash
# Use this script when the host's loader is incompatible with shipped libc.
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do
  DNAME=$(dirname "$SOURCE")
  HERE=$(cd -P "$DNAME" >/dev/null 2>&1 && pwd)
  SOURCE=$(readlink "$SOURCE")
  [[ "$SOURCE" != /* ]] && SOURCE="$HERE/$SOURCE"
done
DNAME=$(dirname "$SOURCE")
HERE=$(cd -P "$DNAME" > /dev/null 2>&1 && pwd)
exec -a socketserver "$HERE/lib/ld-linux.so" --library-path "$HERE:$HERE/lib" "$HERE/socketserver" "$@"
