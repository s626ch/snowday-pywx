# Snowday-PyWx
Script that scrapes info from weather.com about your current location.

<b>PLEASE check the config file.<br>It's important to have the script run.</b>

# Requirements
- `smtplib`
- `os` & `sys`
- `selenium`
- `shutup`

install with `pip3 install selenium shutup`

# Config File - `wxconfig.py`
Stuff that needs configured for the script to work properly:
- `mailsrvr` - The address to the Mail server used to <b>SEND</b> the messages.
- `mailport` - The port of the Mail server used to <b>SEND</b> the messages.
- `email` - <b>Your</b> email address being used to <b>SEND</b> the messages.
- `paswd` - <b>Your</b> password for the above email address.
- `sendmail` - <b>True</b>/<b>False</b> <u>only</u> variable to enable sending to an email address.
- `sndtoadr` - The email address to send messages <b>TO</b>.
- `sendphon` - <b>True</b>/<b>False</b> <u>only</u> variable to enable sending to a phone number.
- `phonecar` - The phone carrier of the recieving number, options provided in `wxconfig.py`.
- `phonenum` - The phone number, as raw numbers, ex: 5551239191.
- `wxlocation` - The string of your location provided by weather.com<br>
For example, here's one for Cleveland, OH:<br>
5663001387bf7b41425be3b42611a9b6c9de0dcdcd373364527af6ae7cc9477f
- `wxurl` - The one part of the config that should be left <b>AS IS</b>, this adds the location code to weather.com's ten-day URL.

<b><br>Important!</b> - `sendmail` and `sendphon` can <i>both</i> be set to True or False at the same time, to enable sending to both, or disable sending all-together.
