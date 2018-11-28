# LLRN Standard Python Distribution

Author: [Ian A Dalton](https://github.com/ianad/)

Updated: 2018-11-28

## Usage

To install basic analytical toolkit distribution on a fresh python (preferably Python >= 3.4) install:

1. Download and extract or `git clone` this repository to the desktop or other clean workspace
2. Open a Terminal window (Mac OS) or `cmd.exe`/`powershell.exe` in the new directory
    1. Shift + Right-click on Windows, and "open command window/PowerShell here", or open it by launching `cmd.exe`/`powershell.exe` and navigating with `cd` to the extracted `llrn-utils` directory.
3. You're probably best off testing your Python version:
    1. `python --version` to see if the version you are expecting responds.
        1. If you're running Mac OS, this may default to a native Python2, which may or may not have `pip` installed.
        2. If so, try `python3 --version`. If the response here is the version you expected, use `python3` for the commands in the next step instead of `python`
4. Type the following commands to upgrade pip and run the installation:
    1. `python -m pip install --upgrade pip`
    2. `python setup.py install`

If you have don't run into any errors, you can feel free to delete the `llrn-utils` directory and everything in it at this point, but you may want to check your package versions:
1. `pip freeze` to see a list of all installed package versions. Compare these to the list in `requirements.txt`.