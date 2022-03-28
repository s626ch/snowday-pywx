import smtplib
import wxconfig
import os
import sys
from selenium import webdriver
import time
import shutup;shutup.please() #* ignore deprecation warnings for the love of god

def scrapeInfo():
    wxdir = os.getcwd() # get current working directory
    #? multi-platform support
    #! windows
    if sys.platform == 'win32':
        wxdriverpath = os.path.join(wxdir, 'chromedriver.exe')
    #! linux
    if sys.platform == 'linux':
        wxdriverpath = os.path.join(wxdir, 'chromedriverlinux')
    #! mac
    if sys.platform == 'darwin':
        wxdriverpath = os.path.join(wxdir, 'chromedrivermac')
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--log-level=3")
    if sys.platform == 'linux':
        options.add_argument('--remote-debugging-port=6959') #? needed to stop "unknown error: DevToolsActivePort file doesn't exist"
    wxdriver = webdriver.Chrome(executable_path=wxdriverpath, chrome_options=options)

    wxdriver.get(wxconfig.wxurl) #! tell driver to nav to weather site
    time.sleep(1) # give site time to load

    wxtoday = {} #? dictionary for today's results
    #* location you're in
    wxtoday['location'] = wxdriver.find_elements_by_xpath(".//span[@data-testid='PresentationName']")[0].text
    #* accurate as of ...
    wxtoday['time'] = wxdriver.find_elements_by_xpath(".//div[@class='DailyForecast--timestamp--22ExT']")[0].text
    #* day temp, precip, wind...etc.
    wxtoday['weekday'] = wxdriver.find_elements_by_xpath(".//span[@class='DailyContent--daypartDate--2A3Wi']")[0].text
    wxtoday['tempday'] = wxdriver.find_elements_by_xpath(".//span[@class='DailyContent--temp--3d4dn']")[0].text
    wxtoday['precipday'] = wxdriver.find_elements_by_xpath(".//span[@data-testid='PercentageValue']")[1].text
    wxtoday['windday'] = wxdriver.find_elements_by_xpath(".//span[@data-testid='Wind']")[1].text
    wxtoday['phraseday'] = wxdriver.find_elements_by_xpath(".//p[@data-testid='wxPhrase']")[0].text
    wxtoday['wxstatus'] = wxdriver.find_element_by_xpath(".//*[@id='detailIndex0']/div/div[1]/div/div[@data-testid='weatherIcon']/*/*[1]").get_attribute('innerHTML') #? this is grabbing the title within the svg, because i guess xpaths don't recognize most, if not any, semantic html tags
    # ===============================================================================
    print() # blank line to make it look nicer
    print("=" * 60)
    print(f"Weather for: {wxtoday['location']}, accurate {wxtoday['time']}")
    print("=" * 60)
    print(f"{wxtoday['weekday']}")
    print(f"Temperature: {wxtoday['tempday']} - {wxtoday['wxstatus']}")
    print(f"Chance of rain/snow: {wxtoday['precipday']}")
    print(f"Wind: {wxtoday['windday']}")
    print(f"{wxtoday['phraseday']}")

    print() # blank line to make it look nicer
    wxdriver.quit()

    def sendProcess():
        #! login to email
        srvr = smtplib.SMTP(wxconfig.mailsrvr, wxconfig.mailport) # define server
        #! auth
        srvr.starttls()
        srvr.ehlo() #? hello call?
        srvr.login(wxconfig.email, wxconfig.paswd) #* auth with email and pw
        print("Logged in to mail server.") # probably :^)

        #? if/el checking phone/email
        if wxconfig.sendmail == True:
            # send to email addr
            #! prep message
            emailmsg = f'''From: {wxconfig.email}

============================================================
Weather for: {wxtoday['location']}, accurate {wxtoday['time']}
============================================================
{wxtoday['weekday']}
Temperature: {wxtoday['tempday']} - {wxtoday['wxstatus']}
Chance of rain/snow: {wxtoday['precipday']}
Wind: {wxtoday['windday']}
{wxtoday['phraseday']}'''

            srvr.sendmail(wxconfig.email, wxconfig.sndtoadr, emailmsg.encode("utf-8"))
            #print(wxconfig.email, wxconfig.sndtoadr, emailmsg.encode("utf-8"))
            print("Sent message to eMail address.")
            pass
        else:
            pass

        if wxconfig.sendphon == True:
            #! sending to phone
            #? fix temperature string, since the degree symbol shows as '??' on text messages
            wxtempholder = wxtoday['tempday']
            wxtemp = wxtempholder.rstrip(wxtempholder[-1])
            #! prep messages **MESSAGES**, this has to be split up into 2 to account for
            #! truncation on text messages
            #! prep message
            emailmsgA = f'''From: {wxconfig.email}

Weather for: {wxtoday['location']}, 
accurate {wxtoday['time']}
----------
{wxtoday['weekday']}
Temperature: {wxtemp} deg - {wxtoday['wxstatus']}
Chance of rain/snow: {wxtoday['precipday']}
Wind: {wxtoday['windday']}'''
            emailmsgB = f'''From: {wxconfig.email}

Blurb: {wxtoday['phraseday']}'''
            #* check carriers, could make this a switch?? idk
            if wxconfig.phonecar == 'AT&T':
                phoneaddr = wxconfig.phonenum + '@txt.att.net'
                pass
            elif wxconfig.phonecar == 'Boost':
                phoneaddr = wxconfig.phonenum + '@myboostmobile.com'
                pass
            elif wxconfig.phonecar == 'Cricket':
                phoneaddr = wxconfig.phonenum + '@mms.cricketwireless.net'
                pass
            elif wxconfig.phonecar == 'GoogleFi':
                phoneaddr = wxconfig.phonenum + '@msg.fi.google.com'
                pass
            elif wxconfig.phonecar == 'MetroPCS':
                phoneaddr = wxconfig.phonenum + '@mymetropcs.com'
                pass
            elif wxconfig.phonecar == 'Republic':
                phoneaddr = wxconfig.phonenum + '@text.republicwireless.com'
                pass
            elif wxconfig.phonecar == 'Sprint':
                phoneaddr = wxconfig.phonenum + '@pm.sprint.com'
                pass
            elif wxconfig.phonecar == 'TMobile':
                phoneaddr = wxconfig.phonenum + '@tmomail.net'
                pass
            elif wxconfig.phonecar == 'Ting':
                phoneaddr = wxconfig.phonenum + '@message.ting.com'
                pass
            elif wxconfig.phonecar == 'TracFone':
                phoneaddr = wxconfig.phonenum + '@mmst5.tracfone.com'
                pass
            elif wxconfig.phonecar == 'USCellular':
                phoneaddr = wxconfig.phonenum + '@email.uscc.net'
                pass
            elif wxconfig.phonecar == 'Verizon':
                phoneaddr = wxconfig.phonenum + '@vtext.com'
                pass
            elif wxconfig.phonecar == 'Virgin':
                phoneaddr = wxconfig.phonenum + '@vmobl.com'
                pass
            #print(phoneaddr)
            #! send to phone email, needs to be text only no html formatting
            srvr.sendmail(wxconfig.email, phoneaddr, emailmsgA) # .encode("utf-8")
            time.sleep(5) # space out messages, better idea anyway
            srvr.sendmail(wxconfig.email, phoneaddr, emailmsgB) # .encode("utf-8")
            print("Sent messages to Phone address.")
            pass
        else:
            pass

        #? moved this here if user wants to send to both phone + email
        #* prevent early stopping of mail session that can't reauth
        srvr.quit()
        print("Stopping mail session.\n")
    if wxconfig.sendphon == True or wxconfig.sendmail == True:
        sendProcess()
    else:
        pass

scrapeInfo()