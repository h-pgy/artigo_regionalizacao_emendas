import requests
import pandas as pd
import io

def download_csv_as_dataframe(url, **kwargs):
    """
    Downloads a CSV file from the given URL and returns it as a pandas DataFrame.

    Parameters:
        url (str): The URL of the CSV file.
        **kwargs: Additional keyword arguments to pass to pandas.read_csv.

    Returns:
        pd.DataFrame: The downloaded CSV file as a DataFrame.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad HTTP responses
    csv_content = response.text
    return pd.read_csv(io.StringIO(csv_content), **kwargs)