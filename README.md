# AU10TIX Home Work Project

This project is a Python script that interacts with the GitHub API to perform various actions on a GitHub repository. The script uses the `requests` library to make HTTP requests to the GitHub API endpoints.

## Author

- **Ilan Bitan**
- **ID: 205792187**

## Getting Started

Before running the script, make sure you have the necessary dependencies installed. You can install them using the following command:

```bash
pip install requests
```

## Configuration

In the script, you'll find several constants that need to be configured:

- `GITHUB_API_BASE_URL`: The base URL for the GitHub API.
- `REPO_OWNER`: The owner of the GitHub repository.
- `REPO_NAME`: The name of the GitHub repository.
- `LABEL_NAME`: The label used for filtering issues.
- `ASSIGNEE`: The GitHub user assigned to issues.
- `ACCESS_TOKEN`: The GitHub Personal Access Token for authentication.

## Running the Tests

The script includes several test functions that demonstrate interactions with the GitHub API. To run the tests, execute the script:

```bash
python <script_name>.py
```

Replace `<script_name>` with the name of your Python script.

## Test Functions

1. **test_get_all_open_issues**: Fetches all open issues from the GitHub repository.

2. **test_get_issues_with_label**: Fetches issues with a specific label.

3. **test_create_new_issue**: Creates a new issue in the GitHub repository.

4. **test_verify_new_issue**: Verifies the creation of a new issue.

5. **test_update_issue**: Updates the state of a specific issue (closes it).

6. **test_verify_closed_issue**: Verifies the closure of an issue.

## Important Note

Ensure that your GitHub Personal Access Token (`ACCESS_TOKEN`) has the necessary permissions to perform the actions in the script.

---

Feel free to customize this README to provide more details or instructions specific to your project.
