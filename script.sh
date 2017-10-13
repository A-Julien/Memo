#!/bin/sh

UPSTREAM=${1:-'@{u}'}

LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

if [ $LOCAL = $REMOTE ]; then
    echo "Up-to-date"
elif [ $LOCAL = $BASE ]; then
    git pull
    for f in *; do
    	if [[ -d $f ]] && [ "$f" != "config" ]; then
    		echo "compilation of "$f" file"
    		pwd
       		pandoc -s -S --toc -c ../pandoc.css $f/README.md  -o config/generate/$f"_memo".html
		fi
	done
elif [ $REMOTE = $BASE ]; then
    echo "Need to push"
else
    echo "Diverged"
fi