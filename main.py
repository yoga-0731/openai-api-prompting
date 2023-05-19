# First Prompt
import openai
from api_key import api_key
openai.api_key = api_key

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.8
    )
    return response.choices[0].message["content"]

prompt = f"Create 5 random book titles, book authors and genre and provide the output in a JSON format"
response = get_completion(prompt)
print(response)


# Installing openai pip package

# import sys
# print(sys.executable) - O/P: path

# Use this path to install openai
# Ex: >{path} -m pip install openai
