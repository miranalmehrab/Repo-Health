from repo_activeness import RepoActiveness
from repo_debug_performance import RepoDebugPerformance


def main():
    # activeness = RepoActiveness()
    # activeness.combine_commits_issues()

    debug_performace = RepoDebugPerformance()
    debug_performace.combined_opened_closed_issues()

if __name__ == "__main__":
    main()