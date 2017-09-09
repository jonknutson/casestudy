Usage:
This program was developed using Python 2.7.12 in a Python virtual environment. No special module installation is
required in order to run.

Reporting file usage on a mountpoint:
From the root of the project, run:
python ./src/get_disk_usage.py [mountpoint]
e.g. python ./src/get_disk_usage.py /tmp

Output is returned as a formatted JSON string.

Testing:
Testing requires pytest, mock, and robber. To install, from the root directory run:
pip install -Ur requirements.txt

Testing is focused on construction of the dictionary object and uses mocks to achieve deterministic results. I considered
using a test directory structure, but running the program on different filesystems could potentially impact the results.

Thoughts on improvements:
The program as defined does not seem particularly useful, but that is partly due to my strict interpretation of the
"requirements." When a filesystem fills up, I should want to be able to quickly identify the largest files. Sorting by,
and outputing the largest files, or largest directories, could help achieve the real goal of identifying how to free
up space on the filesystem.

Another issue that is very possible is overflows for filesystems with very large object counts. I considered implementing
as a Generator (Iterable), and writing output line-by-line to file, but I wasn't sure that met the intended results.
Alternatively, I'd store the results in a key:value database, like redis, LevelDB.
