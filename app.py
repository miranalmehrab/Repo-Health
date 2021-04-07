import json


def get_csv_contents(filename):
    fp = open('data/'+filename, 'r')
    contents = fp.read()
    contents = contents.split('\n')
    
    contents.pop()
    return contents

def convert_str_to_dict(contents):
    dict_contents = []
    for content in contents:
        dict_contents.append(json.loads(content))

    return dict_contents

def find_commits_per_month():
    commits_per_month = []
    contents = get_csv_contents('commits.csv')
    contents = convert_str_to_dict(contents)

    for content in contents:
        if content['committer_commit_date']:
            year_month_day = content['committer_commit_date'].split("T")[0]
            year_month = year_month_day.split("-")[0]+'-'+year_month_day.split("-")[1]
            
            year_month_already_included = False

            for month in commits_per_month:
                if month[0] == year_month:
                    month[1] = int(month[1]) + 1
                    year_month_already_included = True
                    break
            
            
            if year_month_already_included is False:
                commits_per_month.append([year_month, 1])

    commits_per_month.sort(key = lambda x: x[0])
    
    print(['month', 'commits'])
    for item in commits_per_month:
        print(item)



def main():
    find_commits_per_month()    

if __name__ == "__main__":
    main()