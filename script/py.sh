
#!/bin/bash
while :
do
    python3 url.py 
    sleep 5
    sh TextClassification/main.sh
    sleep 5
done
