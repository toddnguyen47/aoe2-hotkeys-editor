# aoe2_hotkeys_editor
A fork of crimsoncantab's [AoC Hotkey Editor](https://github.com/crimsoncantab/aok-hotkeys) with some of my personal edits. All credits go to [crimsoncantab](https://github.com/crimsoncantab/)'s wonderful code. He wrote everything in the `modules` folder.

# Requirements
You will need to download and install [Python 2.7](https://www.python.org/downloads/). Note that Python 3 will most likely not work.

# How to Run
1. Change `params.py` parameters as needed.
2. To read in a HKI file, type into a command line
```
python main.py read
```
3. To change the read HKI file, go into `hki_files/` and change the exported text file from step 2.
4. To export, type into a command line
```
python main.py write
```

# How to Place into your Steam Directory
1. Go into where you installed Steam and Age of Empires 2. Usually, it is located at `C:\Program Files (x86)\Steam\steamapps\common\Age2HD\profiles`
2. **IMPORTANT:** Make a backup of your `profile0.hki` file in case anything goes wrong! One way to make a backup is to copy `profile0.hki` file into another directory elsewhere.
3. After you made a backup of `profile0.hki`, place your newly exported hki file in this directory. Rename this new file `profile0.hki`, effectively replacing the old hki file.
4. Boot up Age of Empires 2. You should be good to go!
