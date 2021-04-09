import json
from datetime import date, timedelta
from utilities import get_csv_contents, convert_str_to_dict

class RepoDebugPerformance:

    def __init__(self):
        self.time_to_resolve_issues = []
        self.issues_opened_per_month = []
        self.issues_closed_per_month = []
        self.issue_opened_closed_per_month = []
        self.time_to_resolve_issues_in_a_quarter = []


    def find_issue_opened_per_month(self):
        contents = get_csv_contents('issues.csv')
        contents = convert_str_to_dict(contents)

        for content in contents:
            if content['created_at']:
                year_month_day = content['created_at'].split("T")[0]
                year_month = year_month_day.split("-")[0]+'-'+year_month_day.split("-")[1]
                
                year_month_already_included = False

                for month in self.issues_opened_per_month:
                    if month[0] == year_month:
                        month[1] = int(month[1]) + 1
                        year_month_already_included = True
                        break
                
                
                if year_month_already_included is False:
                    self.issues_opened_per_month.append([str(year_month), 1])

        self.issues_opened_per_month.sort(key = lambda x: x[0])
        
        # print(['month', 'opened issues'])
        # for item in self.issues_opened_per_month:
        #     print(item)
    

    def find_issue_closed_per_month(self):
        contents = get_csv_contents('issues.csv')
        contents = convert_str_to_dict(contents)

        for content in contents:
            if content['closed_at']:
                year_month_day = content['closed_at'].split("T")[0]
                year_month = year_month_day.split("-")[0]+'-'+year_month_day.split("-")[1]
                
                year_month_already_included = False

                for month in self.issues_closed_per_month:
                    if month[0] == year_month:
                        month[1] = int(month[1]) + 1
                        year_month_already_included = True
                        break
                
                
                if year_month_already_included is False:
                    self.issues_closed_per_month.append([str(year_month), 1])

        self.issues_closed_per_month.sort(key = lambda x: x[0])
        
        # print(['month', 'closed issues'])
        # for item in self.issues_closed_per_month:
        #     print(item)
    
    
    def combined_opened_closed_issues(self):
        self.find_issue_opened_per_month()
        self.find_issue_closed_per_month()

        for opened_issue in self.issues_opened_per_month:
            opened_issue_month = opened_issue[0]
            opened_issue_count = opened_issue[1]

            for closed_issue in self.issues_closed_per_month:
                if closed_issue[0] == opened_issue_month:
                    closed_issue_count = closed_issue[1]
                    self.issue_opened_closed_per_month.append([str(opened_issue_month), opened_issue_count, closed_issue_count, float(opened_issue_count*1.00 / closed_issue_count*1.00)])
                    break
            
        print('combine_issue_open_and_close length '+str(len(self.issue_opened_closed_per_month)))
        print(['month', 'opened issues', 'closed issues', 'opened / closed issues ratio'])

        for open_closed in self.issue_opened_closed_per_month:
            print(open_closed)
    

    def average_time_to_resolve_an_issue_in_quarter_year(self):
        issues = get_csv_contents('issues.csv')
        issues = convert_str_to_dict(issues)
        
        for issue in issues:
            created_at_date = None
            closed_at_date = None

            if issue['number'] and issue['created_at'] and issue['closed_at']:
                created_at_date = str(issue['created_at'].split("T")[0])
                closed_at_date = str(issue['closed_at'].split("T")[0])
                
                created_at_date_splits = created_at_date.split('-')
                f_date = date(int(created_at_date_splits[0]), int(created_at_date_splits[1]), int(created_at_date_splits[2]))
                
                closed_at_date_splits = closed_at_date.split('-')
                l_date = date(int(closed_at_date_splits[0]), int(closed_at_date_splits[1]), int(closed_at_date_splits[2]))

                date_diff = l_date - f_date
                self.time_to_resolve_issues.append([issue['number'],created_at_date, closed_at_date, date_diff.days+1])
        
        self.time_to_resolve_issues.sort(key = lambda x: x[0])

        # print("len of time_to_resolve_issues: "+str(len(time_to_resolve_issues)))
        # for time_to_resolve in self.time_to_resolve_issues:
        #     print(time_to_resolve)
        
        oldest_year_month_date = date(int(self.time_to_resolve_issues[0][1].split('-')[0]), int(self.time_to_resolve_issues[0][1].split('-')[1]), int(self.time_to_resolve_issues[0][1].split('-')[2]))
        newest_year_month_date = date(int(self.time_to_resolve_issues[-1][1].split('-')[0]), int(self.time_to_resolve_issues[-1][1].split('-')[1]), int(self.time_to_resolve_issues[0][1].split('-')[2]))
        delta = timedelta(days=30)

        while oldest_year_month_date <= newest_year_month_date:
            oldest_year_month_date += delta
            self.time_to_resolve_issues_in_a_quarter.append([oldest_year_month_date , 0, 0, 0.00])    
        
        # for quarter_month in self.time_to_resolve_issues_in_a_quarter:
        #     print(quarter_month)

        for time_to_resolve in self.time_to_resolve_issues:
            curr_issue_date_splits = time_to_resolve[1].split("-")
            curr_date = date(int(curr_issue_date_splits[0]), int(curr_issue_date_splits[1]), int(curr_issue_date_splits[2]))
            
            for quarter_month in self.time_to_resolve_issues_in_a_quarter:
                if curr_date <= quarter_month[0]:
                    quarter_month[1] += 1
                    quarter_month[2] += time_to_resolve[3] 
                    break
            
        print(['Quarters', 'No of created issues', 'Total time required in day(s)', 'Average time required in day(s)'])
        for quarter_month in self.time_to_resolve_issues_in_a_quarter:
            if quarter_month[1] != 0:
                quarter_month[3] = quarter_month[2]*1.00 / quarter_month[1]*1.00
            
            print(quarter_month)

        # [date-q1 2016, total no of commits, total time required]

        # for time_to_resolve in self.time_to_resolve_issues:
        #     year_month = time_to_resolve[1].split('-')[0] +'-'+ time_to_resolve[1].split('-')[1]
        #     print(year_month)