#!/bin/bash
git pull
rm /home/pi/Memo/config/compile/*.html
for f in *; do
	if [[ -d $f ]] && [ "$f" != "config" ]; then
    		echo "compilation of "$f" file"
    		pwd
       		pandoc -s -S --toc -c ../pandoc.css /home/pi/Memo/$f/README.md  -o /home/pi/Memo/config/compile/$f"_memo".html
	fi
done
python /home/pi/Memo/engine.py
sudo cp /home/pi/index.html /var/www/html/
