from jira import JIRA

# define jira server
options = {
    'server':'https://example.com'
}

#TODO: remove usename/pw
jira = JIRA(options, basic_auth=('someone_name@domain.com', 'ZYX_PASSWORD'))



test_jira = jira.search_issues('project=RPM and fixversion=15.2.CP')


print(test_jira)










#projects = jira.projects()
#issue = jira.issue('RDOPS-XXXX')

#print(projects)
#print(f'issue: {issue.fields.summary} ')







#JIRA Project: key='RPM', name='RPM', id='10315'

# hd_data = ['Enable Technical Release','Display Currency in Currency Pair']

# create_data_collector = []

# for i in range(len(hd_data)):

#     issue_dict = {
#         'project': {'id': 10315},
#         'summary': hd_data[i],
#         'description': hd_data[i],
#         'issuetype': {'name': 'RPM Project'},
#     }

#     create_data_collector.append(issue_dict)

# #new_issue = jira.create_issue(fields=issue_dict)

# issues = jira.create_issues(field_list=create_data_collector)

# #print(create_data_collector)
