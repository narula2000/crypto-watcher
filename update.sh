#!/bin/bash

TIMEFORMAT='Time took: %5R seconds'

echo "Computing..."
echo "\`\`\`" > out.txt
time pipenv run python3 main.py >> out.txt
echo "\`\`\`" >> out.txt
cat out.txt | xclip -selection clipboard
