import os
import requests  
from Connectedـfunction import get_notion_headers, get_table_id  


page_name = "page1"
table_name = "table1"

table_id = get_table_id(page_name, table_name)

def test_connection():
    if not table_id:
        return "Table ID not found. Please check the page and table names."
    
    url = f"https://api.notion.com/v1/databases/{table_id}"
    response = requests.get(url, headers=get_notion_headers())
    
    if response.status_code == 200:
        return "Connection to Notion is successful!"
    else:
        return f"Failed to connect to Notion. Status Code: {response.status_code}, Response: {response.text}"

print(os.listdir('.'))
result = test_connection()
print(result)