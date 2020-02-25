## Problem 1

**1. Create table `Books` for <span style="color: crimson !important">data/books/books.json</span> with following inputs**
  - Partition Key: Publisher
  - Sort Key: Title
  - Global Secondary Index: ISBN

**2. Add a book using `put item`**

**3. Add all the rest of the books using `batch write`**

**4. Get book <span style="color: crimson !important">Learning JavaScript Design Patterns</span> published by <span style="color: crimson !important">O'Reilly Media</span>**

**5. Get book with ISBN number <span style="color: crimson !important">9781491904244</span>**

**6. Update pages of book <span style="color: crimson !important">Git Pocket Guide</span> published by <span style="color: crimson !important">O'Reilly Media</span> to <span style="color: crimson !important">268</span>**

**7. List out book `titles` with `pages` with more than <span style="color: crimson !important">300</span> pages**

## How to Run Solution
To run the python programs, grab a copy of the current directory
from GitHub. After that, get the latest version of `python` and install `boto3` using following command
```console
pip install boto3
```
Now, all you have to do is run the following command from the command line:
```console
python q#.py
```
where # will be the number of question  you want to run.

