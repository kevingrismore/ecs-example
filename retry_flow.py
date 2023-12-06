from prefect import flow

from google.auth.transport.requests import Request
from google.auth import exceptions
from google.auth.credentials import Credentials


@flow()
def main():
    credentials = Credentials.from_service_account_file("YOUR_JSON_KEY_FILE.json")

    try:
        # Attempt to refresh the token
        credentials.refresh(Request())
    except exceptions.RefreshError as e:
        print(f"Error refreshing the token: {e}")


if __name__ == "__main__":
    main()
