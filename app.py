import pandas as pd

# Load the old and new Excel files
old_file_path = 'path_to_old_file.xlsx'  # Update with the path to your old Excel file
new_file_path = 'path_to_new_file.xlsx'  # Update with the path to your new Excel file

# Read the Excel files into pandas DataFrames
old_df = pd.read_excel(old_file_path)
new_df = pd.read_excel(new_file_path)

# 'IP Address' is the column to match on and 'Secret Server' is the column with the URLs
# Create a dictionary from the old DataFrame with IP Addresses as keys and Secret Server URLs as values
url_mapping = dict(zip(old_df['IP Address'], old_df['Secret Server']))

# Define a function to apply the mapping
def get_url_from_old(ip_address):
    return url_mapping.get(ip_address, None)  # Returns None if the IP address is not found

# Apply the function to the 'IP Address' column in the new DataFrame to create a new 'Secret Server' column
new_df['Secret Server'] = new_df['IP Address'].apply(get_url_from_old)

# Save the updated new DataFrame to a new Excel file
new_file_path_updated = 'path_to_new_file_with_urls.xlsx'  # Update with the desired path for the updated new Excel file
new_df.to_excel(new_file_path_updated, index=False)  # Set index=False to avoid writing row indices
