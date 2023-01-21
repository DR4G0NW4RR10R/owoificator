# owoificator

The owoificator is a tool that takes what you type,
and turns it into owo-compatible text.


## Getting started

You will need to install Python (lastest "3" version preferable),
and the pynput library. You can install the pynput library
by running the following command in your terminal:

> pip3 install pynput

After that, you should be ready to go!


## Using the owoificator

Here's how to use the owoificator!

### Starting the key listener {starting}

first, run `main.py`. You can do this by navigating to the
directory it is in in your terminal, then running this command:

> python3 main.py

However, you can also double click the `main.py` file to run it,
if you are on Windows.

Once the script is running, it will listen for your key presses and
log them in the `keylog.txt` file. It will be as if you are also
typing in that file at the same time.

### Stopping the key listener

To stop the key listener, you can either close the terminal window
that is running the script, or you can press CTRL+C while focused
on the terminal window running the script. If neither of those work,
your computer's Task Manager should be able to get the job done.
(Force Quit on Mac)

### owoifying your text {owoifying}

To owoify what is in the `keylog.txt` file, simply run the `owoify.py`
script. You can run it in the same manner that you can run the `main.py`
script, as detailed in the [Starting the key listener](#starting) section.

Then open the `keylog.txt` file, and you'll see that the text within has
been successfully owoified!

### owoifying other text

You can also owoify other text. To do so, simply paste the text you want
to owoify into the `keylog.txt` file and run the `owoify.py` script, as
detailed in the [owoifying your text](#owoifying) section.


## Changing the owoification settings

You can change the settings of the owoificator with the `settings.json` file.

- wordFrequency: determines how likely a word is to be owoified, as a decimal. Default is 1 (100% chance).
- replaceL: determines how likely an owoified word is to have every l replaced by a w. Default is 0.5.
- replaceR: determines how likely an owoified word is to have every r replaced by a w. Default is 0.5.
- replaceFer: determines wether or not an owoified word gets "fer" replaced by "fur". Default is true.
- replaceFor: determines wether or not an owoified word gets "for" replaced by "fur". Default is true.
- replaceOw: determines wether or not an owoified word is to get "ow" replaced with "owo". Default is true.
- uwuFrequency: determines how likely a sentence gets "uwu" appended to the end of it uwu. Default is 1 uwu.
- replaceUwuWithOwo: determines how likely an uwu'd senence is to have the uwu replaced by owo. Default is 0 owo.