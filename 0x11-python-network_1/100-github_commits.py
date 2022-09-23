https://developer.github.com/v3/repos/commits/
#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commit = req.json()
    try:
        for x in range(10):
            print("{}: {}".format(
                commit[x].get("sha"),
                commit[x].get("commit").get("author").get("name")))
    except IndexError:
        pass
