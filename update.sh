#!/bin/bash

rm out.txt

echo "Computing..."
start=`date +%s`
echo "\`\`\`" >> out.txt
pipenv run python3 main.py >> out.txt
echo "\`\`\`" >> out.txt
end=`date +%s`
echo "Done..."
runtime=$((end-start))
echo "Time took: $runtime"
cat out.txt | xclip -selection clipboard
