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
        
        print(['month', 'opened issues'])
        for item in self.issues_opened_per_month:
            print(item)
    

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
        
        print(['month', 'closed issues'])
        for item in self.issues_closed_per_month:
            print(item)
    
    
    def combined_opened_closed_issues(self):
        self.find_issue_opened_per_month()
        self.find_issue_closed_per_month()

        for opened_issue in self.issue_opened_closed_per_month:
            month = opened_issue[0]

            for closed_issue in self.issue_opened_closed_per_month:
                if issue[0] == month:
                    self.issue_opened_closed_per_month.append([str(month), opened_issue[1], closed_issue[1]])
                    break
            
        print(len(self.issue_opened_closed_per_month))
        for open_closed in self.issue_opened_closed_per_month:
            print(open_closed)
    