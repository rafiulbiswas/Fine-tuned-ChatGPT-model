import openai 

#define a function to open a file and return its its content as string

def open_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as infile:
            return infile.read()
        
def save_file(file_path,content):
        with open(file_path, 'a', encoding='utf-8') as outfile:
             outfile.write(content)
openai.api_key="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"
file_id="file-awb3mMhKnVrgzvPtvnLmUXTQ"
model_name="gpt-3.5-turbo"

response=openai.FineTuningJob.create(
        training_file=file_id,
        model=model_name
    )
job_id=response['id']
print(f"fine tuned successfully with: {job_id}")

