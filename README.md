# Solution-Downloader
Python scripts to download solutions of "SPOJ" and "CODECHEF"

### Instructions

Requirements for Linux Systems
-------------------------------
* You will need [Python 2](https://www.python.org/download/). 
* [pip](http://pip.readthedocs.org/en/latest/installing.html) is recommended for installing dependencies.
* [RoboBrowser][1]
	- `pip install robobrowser`
* [pathlib][2]
	- `pip install pathlib`
	
To run the scripts clone the repository
* In your terminal run
	- `git clone https://github.com/aakardwivedi/Solution-Downloader.git`
	- `cd Solution-Downloader/`
	- `python python spoj.py`
* Enter your "SPOJ" username and password.
* Solution will be save in a folder named spoj_solutions.
	- `python codechef.py`
* Enter your "CODECHEF" username and password.
* Solutions will be saved in a folder named codechef_solutions.


#### Note

* For downloading codechef solutions please log out of codechef from all existing sessions.
* Codechef to decrease load on its servers restricts the number of requests,
* if all solutions are not downloaded run the command `python codechef.py` again.
* In some systems you might need to add `sudo -H` before pip commands.


_Will add scripts for other platforms soon._

[1]: https://github.com/jmcarp/robobrowser
[2]: https://docs.python.org/3/library/pathlib.html
[3]: https://www.python.org/
