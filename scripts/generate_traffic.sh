
while true; do
   
    ping -c 5 8.8.8.8 > /dev/null
    ping -c 5 1.1.1.1 > /dev/null
    curl -s http://example.com > /dev/null
    dig @8.8.8.8 google.com > /dev/null
    dig @1.1.1.1 facebook.com > /dev/null

    sleep $((RANDOM % 5 + 1))
done 