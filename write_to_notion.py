from notion_client import Client 

notion_token ='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'
notion_page_id = '1e7a17706bc880b4863ffa2d49d3d022'



client = Client(auth=notion_token)

page_response = client.pages.retrieve(notion_page_id)

def write_to_db(name, link):
    response = client.pages.create(
        parent = {"database_id": notion_page_id},
        properties={
        "Name": {
            "title": [
                {
                    "text": {
                        "content": name
                    }
                }
            ]
        },
        "Link": {
            "rich_text": [
                    {
                    "text": {
                        "content": link
                    }
                }
            ]
        }
        }
    )
    

print(page_response) #check connection

