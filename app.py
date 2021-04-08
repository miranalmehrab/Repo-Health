from repo_activeness import RepoActiveness


def main():
    activeness = RepoActiveness()
    activeness.combine_commits_issues()


if __name__ == "__main__":
    main()