#!/bin/bash

# Set the list of websites to check
websites=("www.google.com" "www.facebook.com" "www.twitter.com" "www.apple.com" "www.instagram.com")

# Loop through the websites
for website in "${websites[@]}"
do
    # Check the SSL expiration date using the openssl command
    expiry=$(echo | openssl s_client -servername "$website" -connect "$website":443 2>/dev/null | openssl x509 -noout -dates | grep notAfter | cut -d'=' -f2)
    # certificate=$(echo | openssl s_client -servername "$website" -connect "$website":443 2>/dev/null | openssl x509)

    # Print the website and its SSL expiration date
    echo "$website: $expiry: $certificate" 
done | sort -k2 > log.txt

