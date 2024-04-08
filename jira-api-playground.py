from jira import JIRA
import os

users_dict = {
                    "deep"  : "Deep Mistry",
                    "malav" : "Malav Chauhan",
                    "caleb" : "Caleb Mathew",
                    "dante" : "Dante Randall",
                    "alex"  : "Alexander Wessenberg"
                }

def connect_to_jira():
    try:
        JIRA_KEY = os.environ["JIRA_API_KEY"]
    except:
        print("failed to get the jira key from env")


    jira = JIRA(
                    server="https://deepmistry.atlassian.net/",
                    basic_auth=("mistryman41@gmail.com", JIRA_KEY),
                    
                )
    issue = jira.issue('AE-68', fields='summary,comment')
    
    print("Printing test issue")

    try:
        print(issue)
    except:
        print("Failed to grab the issue")

    return jira


def get_jira_projects(jira):
    projects = jira.projects()
    return projects

def get_jira_issue(jira, issue_str):
    issue = jira.issue(issue_str)
    return issue

def get_jira_issue_specifics(jira, issue_str):
    issue_obj = get_jira_issue(jira, issue_str)
    

    issue_details = {
        "issue_key"  : issue_obj.key,
        "issue_summary" : issue_obj.fields.summary,
        "issue_type" : issue_obj.fields.issuetype,
        "issue_parent" : issue_obj.fields.parent,
        "issue_project" : issue_obj.fields.project,
        "issue_resolution" : issue_obj.fields.resolution,
        "issue_resolutiondata" : issue_obj.fields.resolutiondate,
        "issue_priority" : issue_obj.fields.priority,
        "issue_assignee" : issue_obj.fields.assignee,
        "issue_status" : issue_obj.fields.status,
        "issue_timeoriginalestimate" : issue_obj.fields.timeoriginalestimate,
        "issue_timeestimate" : issue_obj.fields.timeestimate,
        "issue_description" : issue_obj.fields.description,
        "issue_progress" : issue_obj.fields.progress,
        "issue_summary" : issue_obj.fields.summary,
        "issue_timespent" : issue_obj.fields.timespent,
    }
    # issue_summary = issue_obj.fields.summary
    # issue_type = issue_obj.fields.issuetype
    # issue_parent = issue_obj.fields.parent
    # issue_project = issue_obj.fields.project
    # issue_resolution = issue_obj.fields.resolution
    # issue_resolutiondata = issue_obj.fields.resolutiondate
    # issue_priority = issue_obj.fields.priority
    # issue_assignee = issue_obj.fields.assignee
    # issue_status = issue_obj.fields.status
    # issue_timeoriginalestimate = issue_obj.fields.timeoriginalestimate
    # issue_timeestimate = issue_obj.fields.timeestimate
    # issue_description = issue_obj.fields.description
    # issue_progress = issue_obj.fields.progress
    # issue_summary = issue_obj.fields.summary
    # issue_timespent = issue_obj.fields.timespent

    return issue_details


def list_completed_issues(jira):
    comepleted_issues_in_proj = jira.search_issues('project = "AE" AND status = "Met Scope"') #AND assignee = "Deep" ORDER BY created DESC')
    
    completed_issues_list = []
    
    for iter in comepleted_issues_in_proj:
        print(iter.key)
        completed_issues_list.append(iter.key)

    return completed_issues_list


def return_reducedlist_assignedto_user(jira, list_of_issues, user):
    user_specific_issues = []

    for i in list_of_issues:
        issue_specifics = get_jira_issue_specifics(jira, i)
        if issue_specifics.issue_assignee == user:
            user_specific_issues.append(i)
          
    return user_specific_issues

def prettyprint_issuespecifics_and_totaltime(jira, list_of_issues):
    totaltime = 0
    for i in list_of_issues:
        print("user:{0} , completed:{1} , in {2} hours".format(
                                                            i["issue_assignee"], 
                                                            i["issue_key"], 
                                                            i["issue_timespent"], 
                                                            ))
        totaltime = totaltime + i["issue_timespent"]

    print("Total time was: " + totaltime)

jira = connect_to_jira()
issue_obj = get_jira_issue(jira, "AE-94")
issue_dict = get_jira_issue_specifics(jira, "AE-94")
issues_in_proj = jira.search_issues('project=AE')




#project = "AE" AND status = "Met Scope"  AND assignee != "Deep" ORDER BY created DESC
# project = "AE" AND status = "In Progress"  AND assignee != "Deep" ORDER BY created DESC
comepleted_issues_in_proj = jira.search_issues('project = "AE" AND status = "Met Scope"') #AND assignee = "Deep" ORDER BY created DESC')
list_of_completed_issues = list_completed_issues(jira)


alexs_issues = return_reducedlist_assignedto_user(jira, list_completed_issues, users_dict['alex'])


import pdb
pdb.set_trace()

