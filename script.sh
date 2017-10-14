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
       		pandoc -s -S --toc -c /home/pi/Memo/config/pandoc.css /home/pi/Memo/$f/README.md  -o /var/www/html/Memo/$f"_memo".html
		fi
	done
	python /home/pi/Memo/engine.py
elif [ $REMOTE = $BASE ]; then
    echo "Need to push"
else
    echo "Diverged"
fi
