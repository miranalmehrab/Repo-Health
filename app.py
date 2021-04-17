from repo_activeness import RepoActiveness
from repo_debug_performance import RepoDebugPerformance


def main():
    activeness = RepoActiveness()
    # activeness.find_commits_per_month()
    activeness.issue_opened_per_month()
    # activeness.combine_commits_issues()

    # debug_performace = RepoDebugPerformance()
    # debug_performace.combined_opened_closed_issues()
    # debug_performace.average_time_to_resolve_an_issue_in_quarter_year()

if __name__ == "__main__":
    main()