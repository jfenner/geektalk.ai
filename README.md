# Geektalk.ai

Welcome to the Geektalk.ai repository! This project is a proof of concept for integrating ChatGPT (specifically `gpt-3.5-turbo` and `DALL-E`)to Wordpress in order to generate articles and images associated with them.

You can view the code in action at https://geektalk.ai

## Getting Started

To get started, copy the `.env.template` file to `.env` and configure it with your data.  your actual key:

```
LOGGING_LEVEL=INFO
OPENAI_API_KEY=<your openai api key>
WP_BASE_URL=<your wordpress base url>
WP_USERNAME=<your wordpress username>
WP_PASSWORD=<your wordpress application password>
```

Next, you'll need to install the required dependencies. You can do this by running the following command:

```
pip install -r requirements.txt
```

After that, simply run the `geektalk.py` file to start the chatbot:

```
python geektalk.py
```

## Usage

Once the chatbot is running, you can start engaging in conversation with it by typing in your messages. The chatbot will respond with its own messages based on the context of the conversation. You can talk about a wide range of topics, including movies, TV shows, video games, comic books, and more.

## Contributing

We welcome contributions to this project! If you'd like to make a contribution, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.