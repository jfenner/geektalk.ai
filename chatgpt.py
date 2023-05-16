import logging
import openai

#
# Class to handle the ChatGPT API
#


class ChatGPT:
    def __init__(self, api_key) -> None:
        openai.api_key = api_key

    def __str__(self) -> str:
        return "ChatGPT"

    # Generate the content from the prompt with ChatGPT
    def generateContent(self, prompt):
        # Set the model ID for GPT-3.5-Turbo
        model_engine = "gpt-3.5-turbo"

        # Send the request to the API
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        logging.debug(response)

        content = response.choices[0].message.content.strip("\"")
        return content

    # Generate an image from the prompt with ChatGPT
    def generateImage(self, prompt):
        # Send the request to the API
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        return response.data[0].url
