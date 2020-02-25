## Problem 2

**1. Create a table `WebAccessLog` for <span style="color: crimson">data/logs/web_access_log.json</span> with following constraints:**

- Partition Key: `ip_addr`
- Sort Key: `req_no`


**2. Write script to perform batch writes with batch size of 25 items for all log items ( i.e 201 entries )**

**3. For IP address `188.45.108.168`, give count of requests that have not returned status `200`**

**4. For IP address `191.182.199.16`, give daily count of requests, and daily total data (size) downloaded**

---

<div style="page-break-after: always;"></div>

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

