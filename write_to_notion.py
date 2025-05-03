from notion_client import Client #type: ignore

notion_token ='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'
notion_page_id = '1e7a17706bc880b4863ffa2d49d3d022'

def write_text(client, page_id, text):
    pass

client = Client(auth=notion_token)

page_response = client.pages.retrieve(notion_page_id)

print(page_response) #check connection
