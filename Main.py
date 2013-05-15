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

    # Now open website and do the things needed
    site = br.open('http://202.65.142.140/CFSTONLINE/Reports/VehicleRegistrationSearch.aspx')

    # Build the regular expression
    data_notfound_regex = re.compile('<span id="ctl00_OnlineContent_lblMsg" class="errormsg">No Data Found</span></td>', re.MULTILINE)
    data_found_regex = re.compile('<span id="ctl00_OnlineContent_lblMsg"></span></td>', re.MULTILINE)
    data_found_regex2 = re.compile('<span id="ctl00_OnlineContent_lblMsg" class="errormsg"></span></td>', re.MULTILINE)

    ## forms
    #for f in br.forms():
        #print f

    # File pointer to the source of the Engine No's
    engine_nos_fp = open("engine_nos.txt", mode= 'r')

    # File pointer for adding Registered No's
    registered_fp = open("registered_nos.txt", mode= 'w')

    for engine_no in engine_nos_fp:

        # select specific form - here first form (index 0)
        br.select_form(nr=0)

        # Now fill the static data to the form
        br.form['ctl00$OnlineContent$ddlInput'] = ['E']

        # Fill the data that changes for each submission
        if engine_no != None:
            br.form['ctl00$OnlineContent$txtInput'] = engine_no.strip()
        else:
            break

        # Check if the vehicle is registered or not
        try:
            # Submit the form and get the data
            res = br.submit()

            # Read the line that decides if vehicle is registered
            line = res.readlines()[121].strip()
            print line

            # Match the Reg Ex
            line_match_notfound = data_notfound_regex.match(line)
            line_match_found = data_found_regex.match(line)
            line_match_found2 = data_found_regex2.match(line)

            # Check for registration
            if line_match_notfound != None :

                # Engine No. not registered
                print engine_no.strip(), "Not Registered"

            elif line_match_found != None or line_match_found2 != None:

                # Engine No. is Registered
                registered_fp.write(engine_no)
                print engine_no.strip(), "Registered"

            else:
                print "Error: Reg Ex match line not found !! Check the code!"

        except Exception as ex:
            print "Exception: ", ex
            return 1

        ## printing the results
        #print br.response().read()

    registered_fp.close()
    engine_nos_fp.close()
    print "Job Done!"
    return 0


if __name__ == "__main__":
    main()
