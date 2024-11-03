import requests

NOTION_TOKEN = "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"
TABLE_IDS = {
    "page1": {
        "table1": "13336257ee60802bb336cbc1aeb3aaf8",  
        #"table2": "" 
    }#,
    #"page2": {
    #    "table3": "",  
    #    "table4": ""   
    #}
}


def get_notion_headers():
    headers = {"Authorization": f"Bearer {NOTION_TOKEN}", "Content-Type": "application/json", "Notion-Version": "2022-06-28"}
    return headers


def get_table_id(page_name, table_name):
    return TABLE_IDS.get(page_name, {}).get(table_name)


def test_connection():
    url = "https://api.notion.com/v1/databases"
    response = requests.get(url, headers=get_notion_headers())
    
    if response.status_code == 200:
        return "Connection to Notion is successful!"
    else:
        return f"Failed to connect to Notion. Status Code: {response.status_code}, Response: {response.text}"