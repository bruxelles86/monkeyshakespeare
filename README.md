# monkeyshakespeare
longestMatchLength = 0
longestMatch = ""

while true do

# Generate random keystroke
# E

# For each file, push sentences where first chracter is an E to an array

# Generate random keystroke
# I

# For each file, push sentences where second character is I to an array

# Continue until random keystroke has no matches

# match = whatever the longest string we've got so far ("EI")

# Find new match
    if match.length > longestMatch do
        longestMatchLength = match.length

    end

end
 
#Simlilar attempts link https://www.telegraph.co.uk/technology/news/8789894/Monkeys-at-typewriters-close-to-reproducing-Shakespeare.html

#To run server 
# export FLASK_APP=server.py
# $ python -m flask run
######
#export FLASK_APP=controller.py
#export FLASK_ENV=development
#flask run
#####
created a shell file to run all above commands 
#to run the app use `bash start.sh`

Things that need solving are:
- issue of paraller process: i.e server to response with longest match whilst monkey typed matched keystrokes  keep redefining longest match. 
- Theres seems to be issue with randomness as matched words keep on re apearing 
