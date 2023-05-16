import requests
import json
import logging

#
# Class to handle the Wordpress API
#


class Wordpress:
    def __init__(self, wp_base_url, wp_username, wp_password) -> None:
        self.wp_media_url = wp_base_url + "/wp-json/wp/v2/media"
        self.wp_posts_url = wp_base_url + "/wp-json/wp/v2/posts"
        self.wp_auth = (wp_username, wp_password)

    def __str__(self) -> str:
        return "Wordpress " + self.wp_base_url

    # Upload the image to Wordpress
    def uploadImageToWordpress(self, filename, image_url):
        # Download the image
        response = requests.get(image_url)

        # Prepare the data for the WordPress API request
        image_data = response.content
        headers = {
            "Content-Type": "image/png",
            "Content-Disposition": f"attachment; filename={filename}.png",
        }

        # Upload the image to WordPress
        response = requests.post(
            self.wp_media_url, data=image_data, headers=headers, auth=self.wp_auth)
        response_json = json.loads(response.text)

        # Check response status code
        if response.status_code != 201:
            logging.error(f"Error creating new post: {response.text}")

        return response_json["id"]

    # Post the content to Wordpress
    def postToWordpress(self, title, content, featured_media_id):
        # Post data
        data = {
            "title": title,
            "content": content,
            "featured_media": featured_media_id,
            "author": 1,
            "status": "publish"
        }

        # Send POST request to create new post
        response = requests.post(
            self.wp_posts_url, auth=self.wp_auth, json=data)

        # Check response status code
        if response.status_code != 201:
            logging.error(f"Error creating new post: {response.text}")
