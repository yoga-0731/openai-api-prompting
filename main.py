import openai

from api_key import api_key
openai.api_key = api_key


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message["content"]

messages = [
    {'role': 'system', 'content': 'You are an assistant that speaks like Shakespeare.'},
    {'role': 'user', 'content': 'tell me a joke'},
    {'role': 'assistant', 'content': 'Why did the chicken cross the road'},
    {'role': 'user', 'content': 'I don\'t know'}]
response = get_completion_from_messages(messages, temperature=1)
print(response)

messages = [
    {'role': 'system', 'content': 'You are friendly chatbot.'},
    {'role': 'user', 'content': 'Hi, my name is Ishu'}]
response = get_completion_from_messages(messages, temperature=1)
print(response)

messages = [
    {'role': 'system', 'content': 'You are friendly chatbot.'},
    {'role': 'user', 'content': 'Yes,  can you remind me, What is my name?'}]
response = get_completion_from_messages(messages, temperature=1)
print(response)

messages = [
    {'role': 'system', 'content': 'You are friendly chatbot.'},
    {'role': 'user', 'content': 'Hi, my name is Ishu'},
    {'role': 'assistant', 'content': "Hi Isa! It's nice to meet you. \
    Is there anything I can help you with today?"},
    {'role': 'user', 'content': 'Yes, you can remind me, What is my name?'}]
response = get_completion_from_messages(messages, temperature=1)
print(response)
