# config file -----------------------------------------------------------------------------------------------------------------

# this needs to be set up properly to allow the script to send messages to you
mailsrvr = 'mail2.example.com' # smtp email server address
mailport = 587 # smtp server port
email = 'sender@example.com' # email address
paswd = 'password' # password

# do you want to send it to your email (guaranteed to work),
# or your phone? (results may vary on carrier)
sendmail = False
sndtoadr = 'mail@example.com' # email@site.tld - email to send to if you choose email
sendphon = False
# what's your carrier?
# options: AT&T, Boost, Cricket, GoogleFi, MetroPCS, Republic, Sprint, TMobile, Ting, TracFone, USCellular, Verizon, Virgin
# (i've had success recieving messages from most carriers, except for tmobile, verizon takes ~15 min to relay)
phonecar = 'Verizon' # must be typed exactly as options above
phonenum = '5551239191' # must be typed as JUST the numbers, no area code, no dashes, no parenthesis

# your location, using the code provided from weather.com
wxlocation = '5663001387bf7b41425be3b42611a9b6c9de0dcdcd373364527af6ae7cc9477f'
wxurl = 'https://weather.com/weather/tenday/l/' + wxlocation # full url