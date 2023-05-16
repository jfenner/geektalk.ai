import traceback
from chatgpt import ChatGPT
from wordpress import Wordpress
from decouple import config, Csv
import logging

# Read the config
LOG_LEVEL = config("LOGGING_LEVEL", default="WARNING")
OPENAI_API_KEY=config("OPENAI_API_KEY")
WP_BASE_URL=config("WP_BASE_URL")
WP_USERNAME=config("WP_USERNAME")
WP_PASSWORD=config("WP_PASSWORD")

# Setup logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,  
    datefmt='%Y-%m-%d %H:%M:%S')

logging.info("Starting chatgpt-news.py")
logging.info("LOG_LEVEL: " + LOG_LEVEL)
logging.info("WP_BASE_URL: " + WP_BASE_URL)

# Set up OpenAI
chatGPT = ChatGPT(OPENAI_API_KEY)

# Set up WordPress access
wp_base_url = WP_BASE_URL
wp_username = WP_USERNAME
wp_password = WP_PASSWORD
wordpress = Wordpress(wp_base_url, wp_username, wp_password)

### Main Code ###
style = "Creative"
tone = "Professional"

try:
    # Generate a topic
    topic_prompt = "Give me a geek topic. Limit it to 256 characters."
    logging.info(topic_prompt)
    prompt = chatGPT.generateContent(topic_prompt)
    logging.info(prompt)

    # Generate the title for the article
    title_prompt = "Write a title for an article about '{PROMPT}'. "\
        "Limit it to between 40 and 60 characters. "\
        "Style: {STYLE}. Tone: {TONE}.".format(
            PROMPT=prompt, STYLE=style, TONE=tone)
    logging.info(title_prompt)
    title = chatGPT.generateContent(title_prompt)
    logging.info(title)

    # Generate the sections for the article
    sections_prompt = "Write 2 consecutive headings for an article about '{TITLE}' without numbering them. " \
        "Style: {STYLE}. Tone: {TONE}. " \
        "Limit each header to between 40 and 60 characters. Use Markdown for the headings (## )".format(
            TITLE=title, STYLE=style, TONE=tone)
    logging.info(sections_prompt)
    sections = chatGPT.generateContent(sections_prompt)
    logging.info(sections)

    # Now generate the full content
    content_prompt = "Write an article about '{TITLE}'. The article is organized by the following headings:\n\n" \
        "{SECTIONS}\n\n" \
        "Write 3 paragraphs per heading. "\
        "Use HTML for formatting. " \
        "Add an introduction and a conclusion." \
        "Style: {STYLE}. Tone: {TONE}.".format(
            TITLE=title, SECTIONS=sections, STYLE=style, TONE=tone)
    logging.info(content_prompt)
    content = chatGPT.generateContent(content_prompt)
    logging.info(content)

    # Generate an image and upload it to Wordpress
    image_url = chatGPT.generateImage(prompt)
    logging.info(image_url)
    featured_media_id = wordpress.uploadImageToWordpress(title, image_url)
    logging.info(featured_media_id)

    # And finally, post it all to Wordpress
    wordpress.postToWordpress(title, content, featured_media_id)

except Exception as e:
    logging.error("There was a problem generating the article")
    logging.error(e)
    logging.error(traceback.format_exc())

logging.info("Finished chatgpt-news.py")