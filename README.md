# How to run (Windows)
1. Download the latest release from [here](https://github.com/ddinan/CStrips-Downloader/releases).
2. Extract the file somewhere.
3. In the `dest` folder, run `CStrips-Downloader.exe`.
4. When asked, fill out your **alphanumeric** and ___NOT___ your **numeric** ID. For information on how to get your ID see [the wiki](https://github.com/ddinan/CStrips-Downloader/wiki).

The script should now be running and starting to scan through and download your comics.

# How to find your alphanumeric user ID
If you have forgotten your user ID, there are a few useful methods you can try to find it. See the [wiki](https://github.com/ddinan/cstrips-downloader/wiki) for more information.

# Building from source:
1. Download and install [Python](https://www.python.org/downloads/) _(Standalone CLI app is planned)_.
2. Download [this repository](https://github.com/ddinan/CStrips-Downloader/archive/master.zip).
3. Replace `USER` in [run.py](https://github.com/ddinan/CStrips-Downloader/blob/master/run.py#L16) with yours or your friend's Bitstrips user ID. For example https://bitstrips.com/user/D53J, the ID would be `D53J`.
4. Open your command prompt or terminal _(Type `cmd` into your  Windows search bar)_.
5. `cd` to the folder where you downloaded the script. E.g, `cd C:\Users\Buddy\Desktop\CStrips Downloader`.
6. Type these two commands: `py -m pip install progress` and `py -m pip install requests`.
7. To run the script type the following command: `py run.py`.

The script should now be running and starting to scan through and download your comics.

**KEEP IN MIND:**

`*` There are `60466176` possible combinations to scan for so it **will take a very long time** to download your comics. I did the math for my router and it estimated at around `11.16` days to download all comics but that depends on your internet speed. Feel free to look for ways to make the script faster. If you have any issues regarding installing or running, please make an issue [here](https://github.com/ddinan/CStrips-Downloader/issues) that shows the error or problem you're having.

Enjoy your comics!
