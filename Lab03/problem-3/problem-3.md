## Problem 3

Here you are given a set of data files: Users, Repositories, Commits, Issues
under the directory [data](./data)!

For creating required tables, you have been given a python script q1.py; you can run the script for creating all the required table. Schema information of tables is also given here for your information.

Setup Database
```shell
$ python q1.py # will do required changes
```

**Table Definitions**

**Users** <br>
- Primary Key: `email`

**Repositories**
- Partition Key: `name`
- Sort Key: `owner`
- Global Secondary Index: `repo_id-index`
  - Primary Key: `repo_id`

**Commits**
- Primary Key: `project_id`
- Sort Key: `sha`

**Issues**
- Partition Key: `title`
- Sort Key: `repo_id`
- Local Secondary Index: `reporter-index`
  - Partition Key: `title`
  - Sort Key: `reporter`

**1. Run setup and study the given data**

**2. List all pending issues for the repository `2048` (owner `janet`)**

**3. Find out the latest commit and its author of the repo `linux` which is owned by `torvalds`**

**4. Print list of issue reporters(`name`, `issue_title`) of the repo `toml-lang` owned by `github`**

**5. Run following update queries**

Add a new commit

```json
{
  "sha": "K9QTUE0U3SKDFFKFVP7PMTMQF6GZNEB8NSFH1K",
  "author": "lisa",
  "message": "Resolved an issue from pdf.js",
  "project_id": 4243,
  "timestamp": "2020-02-19T20:40:38Z"
}
```
Set the issue ( `repo-id` = `4243` and `title` = `No Documentation for installation` ) as resolved

**6. List commits (`author_name`) done by the member of
mozilla organization on repo name `pdf.js`**

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

