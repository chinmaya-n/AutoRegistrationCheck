This is a software for testing if a vehicle is registered or not
from the AP Transport registration department.

Using:
-----
* Python
* mechanize python library

Installation:
------------
1. Download and install Python.
   - url: https://www.python.org/downloads/
   - download the latest version and install it   
2. Download and install Mechanize Python Library:
   - url: http://wwwsearch.sourceforge.net/mechanize/download.html
   - Download a stable release, version at the time of writing: mechanize-0.2.5.tar.gz
   - Extract the tar.gz file and copy the "mechanize" directory from the mechanize-X.X.X directory.
   - paste the copied directory to "C:\Program Files (x86)\Python2.X\Lib\site-packages". This finishes
     the mechanize insallation.
3. Now Download the latest release of ARC (Automatic Registration Checker)
	- url: https://github.com/inblueswithu/AutoRegistrationCheck/releases
	- download the latest realease by selecting the ARC_v0.X.X.zip in the Downloads Section (Or) Click the link below
	   Latest Release: https://github.com/inblueswithu/AutoRegistrationCheck/releases/download/v0.1.4/ARC_v0.1.4.zip
4. Crate a directory with name "ARC" and Extract the contents into it.
5. Double click on "Registration Checker.pyc" to run. If it runs properly, Update the file 'engine_nos.txt' with appropriate engine numbers. Registered No's are written to file 'registered_nos.txt'.
6. If step 5 gave any errors which is not meaningful, we have to build an executable for your system. Follow the steps below:
	- Open Python IDLE Console. (Search in Start menu)
	- Type ``` >>> import py_compile ``` in the console & hit enter
	- Type ``` >>> py_compile.compile('H:\ARC\Main.py') ``` in the console & hit enter. Modify the path
		``` H:\ARC\Main.py ``` accordingly for the file we downloaded in step 4.
	- This should produce a file 'Main.pyc' in the same directory.
	- Rename it to remember it, usually "Registration Checker.pyc".
	- Run it to test if its working, if not contact Developer at: ``` inblueswithu@yahoo.co.in ```

Note: Here X - means any number (due to versioning)

Issues:
------
No perfect executable or finished user specific build is not yet generated.
Have to learn how to do that a build with mechanize library & with python libs
inbuild.
