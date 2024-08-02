from openai import OpenAI
 

client = OpenAI(
  api_key="",
)
command ='''
         '''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a real person from india speaks english and analyze chat history and generate reponse to chats"},
    {"role": "user", "command": ""}
  ]
)

print(completion.choices[0].message.content)