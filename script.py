import openai 

#define a function to open a file and return its its content as string

def open_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as infile:
            return infile.read()
        
def save_file(file_path,content):
        with open(file_path, 'a', encoding='utf-8') as outfile:
             outfile.write(content)
openai.api_key="OPENAI API KEY"

with open("output1.jsonl","rb") as file:
    response=openai.File.create(
        file=file,
        purpose='fine-tune'
    )
file_id=response['id']
print(f"file uploaded succesfully:{file_id}")

