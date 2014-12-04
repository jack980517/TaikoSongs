TaikoSongs
==========

Extract M4A files from iOS Taiko no Tatsujin, as well as the info (currently genre &amp; song title only)

This project is written in Python 2 and tested on Python 2.7.3, which is the version available for iDevices on Cydia (apt.178.com)
# Usage:
Create a folder named DAT in the same place as my programs, and put all DAT files from Taiko no Tatsujin in it. Generate a list of files, in the form of "DAT/xxx.dat", name it 00.txt, and put it in the same location too. Create an empty folder named M4A. Then run "python extractor.py" to extract the songs into the M4A folder, and run "python info.py" to extract the info to result.txt.
