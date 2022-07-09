<strong>Name: </strong><em>Name or Tag here</em>
<br>
<strong>Time: </strong> <em>Time here (24hr time)</em>
<br>
<strong>Date: </strong> <em>DD.MM.YY</em>
<br>
<strong>Goal: </strong> <em>Do this before session </em>
<br>
<strong>Description: </strong> <em>What happened</em>

<hr>

<strong>Name: </strong>Arctesian
<br>
<strong>Time: </strong>18:16-20:39
<br>
<strong>Date: </strong> 25.06.22
<br>
<strong>Goal: </strong> Make CSV parser
<br>
<strong>Description: </strong>
Finished everything but the write function, I am tired so I stopped

<hr>

<strong>Name: </strong>Arctesian
<br>
<strong>Time: </strong>12:10-14:21
<br>
<strong>Date: </strong> 05.07.22
<br>
<strong>Goal: </strong> Debug
<br>
<strong>Description: </strong>

The previous log was a lie, I did not finish everything it was a buggy mess. I rewrote from scratch and now only have the write function left. Also wrote the docs after brain stopped working and updating the todo file

<hr>

<strong>Name: </strong>Arctesian
<br>
<strong>Time: </strong>17:03-18:25
<br>
<strong>Date: </strong> 05.07.22
<br>
<strong>Goal: </strong> Write function
<br>
<strong>Description: </strong>

Cleaned up a bunch of shit, made the write function and a bunch of supporting functions, updated docs and wrote comments for everything. Need to pkg for csv format and write tests

<hr>

<strong>Name: </strong>Arctesian
<br>
<strong>Time: </strong>02:03-02:50
<br>
<strong>Date: </strong> 06.07.22
<br>
<strong>Goal: </strong> Multi import support
<br>
<strong>Description: </strong>

Was about to start the release process and realized that i don't have multi import support, I was thinking about doing it with just making the headers mapped to the value of the filename but that passing that around in global states will be a bit of a pain without knowing the name before. I made a filename parser so it would be possible. It is a little late and I still have covid so should sleep but late night thoughts gave me a scare. Will still probs work on setting up the project dir for pypi before I sleep.

<hr>

<strong>Name: </strong>Arctesian
<br>
<strong>Time: </strong>19:33-18:00
<br>
<strong>Date: </strong> 06.07.22
<br>
<strong>Goal: </strong> Upload to pip
<br>
<strong>Description: </strong>

Reconfigured the project so it matches the pypi guidlines. Getting this error when I run tho

```
ERROR: Could not find a version that satisfies the requirement re (from versions: none)
ERROR: No matching distribution found for re
WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
You should consider upgrading via the '/tmp/build-env-tqe2l5b9/bin/python -m pip install --upgrade pip' command.

Traceback (most recent call last):
```

Fixed it by removing `re` in the pyproject.toml file, but this might break it, I only use regex in one function tho so should be fine.

Have everything there now just need to make an account and upload.

Used this [guide](https://www.youtube.com/watch?v=v4bkJef4W94)

<hr>

<strong>Name: </strong>Arctesian
<br>
<strong>Time: </strong>19:33-18:00
<br>
<strong>Date: </strong> 06.08.22
<br>
<strong>Goal: </strong> Upload to pip
<br>
<strong>Description: </strong>

Released, now working on additional features that would be nice
<hr>
