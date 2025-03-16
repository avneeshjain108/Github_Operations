##Python prorgam to get the List of users for an Organiation
import requests

def get_github_enterprise_users(org_name, token, per_page=30):
    users = []
    page_number = 1

    while True:
        # Define the API endpoint
        endpoint = f"https://api.github.com/orgs/{org_name}/members"
        params = {
            "per_page": per_page,
            "page": page_number
        }
        headers = {
            "Authorization": f"token {token}"
        }

        # Make the API request
        response = requests.get(endpoint, headers=headers, params=params)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            break

        # Parse the response and add users
        data = response.json()
        if not data:
            break  # Exit the loop if no more data
        users.extend(data)

        # Increment the page number for the next request
        page_number += 1

    return users


# Example usage
if __name__ == "__main__":
    # Replace with your organization name and personal access token
    ORG_NAME = "your_organization_name"
    TOKEN = "your_personal_access_token"

    # Fetch the users
    users = get_github_enterprise_users(ORG_NAME, TOKEN)

    # Print the user list
    for user in users:
        print(f"Username: {user['login']}, ID: {user['id']}")