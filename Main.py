from bs4 import BeautifulSoup
import mechanize, cookielib, re

def main():
    # Browser
    br = mechanize.Browser()
    
    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    
    # Browser Options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    
    # Follows refresh 0 but not hands on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    
    ## Want debugging messages?
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)
    
    # -- Browser setup done
    site = br.open('https://aptransport.in/APCFSTONLINE/Reports/VehicleRegistrationSearch.aspx')
    
    # File pointer to the source of the Engine No's
    engine_nos_fp = open("engine_nos.txt", mode= 'r')
    
    # File pointer for adding Registered No's
    registered_fp = open("registered_nos.txt", mode= 'w')
    registered_fp.write("--- Registered Vehicles --- \n")
    
    # File pointer for not registered No's
    not_registered_fp = open('not_registered_nos.txt', mode='w')
    not_registered_fp.write("--- NOT Registered --- \n")
    
    try:
        
        # Loop over each engine no and check for the registration
        for engine_no in engine_nos_fp:
            # select specific form - here first form (index 0)
            br.select_form(nr=0)
        
            # Now fill the static data to the form
            br.form['ctl00$OnlineContent$ddlInput'] = ['E']
        
            # Fill the engine_no to test
            engine_no = engine_no.strip()
            if engine_no != None:
                br.form['ctl00$OnlineContent$txtInput'] = engine_no
            else:
                break
            
            # Verbose
            print "Verifying " + engine_no + " ..."
            
            # submit the form and get the required info
            html_page = br.submit().read()
            soup = BeautifulSoup(html_page, 'html.parser')
            wrong_data = soup.find(id="ctl00_OnlineContent_lblMsg")
            vehicle_no = soup.find(id='ctl00_OnlineContent_tdRegnNo')
            owner_name = soup.find(id='ctl00_OnlineContent_tdOwner')
            date_of_reg = soup.find(id='ctl00_OnlineContent_tdDOR')
            
            # Check if vehicle is registered and write to file
            if wrong_data.string == None or wrong_data == "":                
                print_line = engine_no + " : " + vehicle_no.string + " " + \
                    date_of_reg.string + " " + owner_name.string + "\n"
                if len(vehicle_no.string) > 10:
                    not_registered_fp.write(print_line)
                else:
                    registered_fp.write(print_line)
            else:
                print_line = engine_no + " : " + wrong_data.string + "\n"
                not_registered_fp.write(print_line)
    
    # Accept the Exception and Handle it
    except Exception as ex:
        print ex
        print "Please contact the Author of the program. E-Mail: inblueswithu @ yahoo.co.in \
               Mention the above Error in email."
    
    # close the file pointers
    registered_fp.close()
    not_registered_fp.close()
    print "Job Done! Please open 'registered_nos.txt' for all registered vehicles \
           and 'not_registered_nos.txt' for not registered vehicles. \n"
    raw_input("Press Any Key to Exit ...")
    
if __name__ == "__main__":
    main()