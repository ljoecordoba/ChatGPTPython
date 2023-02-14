import openai
import json
with open("config.json") as dictionary:
    config = json.load(dictionary)

openai.api_key = config["api_key"]

completion = openai.Completion.create(engine="text-davinci-003",
                         prompt="Mostrame un ejemplo de saludo en aleman",
                         max_token="2048")
print(completion.choices[0].text)