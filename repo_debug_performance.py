import json
from utilities import get_csv_contents, convert_str_to_dict

class RepoDebugPerformance:

    def __init__(self):
        self.issues_opened_per_month = []
        self.issues_closed_per_month = []
        self.issue_opened_closed_per_month = []


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
    