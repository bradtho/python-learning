#! /bin/bash

curl -s https://www.thewhiskyexchange.com/d/746/rich-fruit-and-spice | pup 'div.name json{}' | jq '. | {"\(.[].text).\(.[].children[]?.text)"}'

#curl -s https://www.thewhiskyexchange.com/d/746/rich-fruit-and-spice | pup 'div.name json{}' | jq -r '. | .[].text'

curl -s https://www.thewhiskyexchange.com/d/746/rich-fruit-and-spice | pup 'div.name json{}' | jq -r '.[] | .children[]?.text'

#curl -s https://www.thewhiskyexchange.com/d/746/rich-fruit-and-spice | pup 'div.name text{}'

jq --argjson span ()

curl -s https://www.thewhiskyexchange.com/d/746/rich-fruit-and-spice | pup 'div.name json{}' | jq -r '.[] | {.text}'

curl -s https://www.thewhiskyexchange.com/d/746/rich-fruit-and-spice | pup 'div.name json{}' | jq '.[] | (.text + " " + .children[]?.text)'  
curl -s https://www.thewhiskyexchange.com/d/746/rich-fruit-and-spice | pup 'div.name json{}' | jq '.[] | "\(.text) \(.children[]?.text)"' > output.json

curl -s https://www.thewhiskyexchange.com/d/746/rich-fruit-and-spice | pup 'div.name json{}' | jq '.'
