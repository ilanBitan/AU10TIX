# ILAN BITAN 205792187

import requests

# Constants
GITHUB_API_BASE_URL = "https://api.github.com"
REPO_OWNER = "topq-practice"
REPO_NAME = "api-practice"
LABEL_NAME = "practice1"
ASSIGNEE = "topq-practice"
ACCESS_TOKEN = "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"

github_api_url = f"{GITHUB_API_BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}"
authentication_header = {"Authorization": f"token {ACCESS_TOKEN}"}


def test_get_all_open_issues():
    response = requests.get(f"{github_api_url}/issues")
    assert response.status_code == 200,\
        f"Failed to get all open issues. Status code: {response.status_code}"
    issues_data = response.json()
    print("\nNumber Of Open Issues:", len(issues_data))


def test_get_issues_with_label():
    response = requests.get(f"{github_api_url}/issues?labels={LABEL_NAME}")
    assert response.status_code == 200, \
        f"Failed to get issues with label. Status code: {response.status_code}"
    issues_data = response.json()
    print("\nNumber Of Issues with Label:", len(issues_data))


def test_create_new_issue():
    issue_data = {
        "title": "Ilan's issue",
        "body": "This issue was created via REST API from Python by Ilan Bitan",
        "labels": [LABEL_NAME],
        "assignees": [ASSIGNEE]
    }
    response = requests.post(f"{github_api_url}/issues", headers=authentication_header, json=issue_data)
    assert response.status_code == 201,\
        f"Failed to create new issue. Status code: {response.status_code}"
    created_issue_data = response.json()
    print("\nNew Issue Number:", created_issue_data["number"])


def test_verify_new_issue():
    response = requests.get(f"{github_api_url}/issues")
    assert response.status_code == 200, \
        f"Failed to get all issues. Status code: {response.status_code}"
    issues_data = response.json()
    assert len(issues_data) == 30, "Number of issues should be initial"
    new_issue = issues_data[0]
    assert new_issue["title"] == "Ilan's issue", "New issue title mismatch"


def test_update_issue():
    issue_number = 1
    update_data = {
        "state": "closed",
        "state_reason": "not_planned"
    }
    response = requests.patch(f"{github_api_url}/issues/{issue_number}",
                              headers=authentication_header, json=update_data)
    assert response.status_code == 200, \
        f"Failed to update issue. Status code: {response.status_code}"


def test_verify_closed_issue():
    response = requests.get(f"{github_api_url}/issues")
    assert response.status_code == 200, \
        f"Failed to get all issues. Status code: {response.status_code}"
    issues_data = response.json()
    assert len(issues_data) == 30, \
        "Total number of issues should be initial (closed issue should not be in the list) + 1 that means: (29+1)==30"
