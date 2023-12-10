import openai
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("openai_token")


def generate_real_estate_post(price, area, bedrooms, bathrooms):
    prompt = f"Price={price}\nArea={area}\nBedrooms={bedrooms}\nBathrooms={bathrooms}\n"
    prompt += "// all parameters used to generate this sample\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    sample_text = response["choices"][0]["message"]["content"].strip()
    return sample_text


def generate_and_save_samples(num_samples=20):
    # Load Housing.csv dataset
    housing_data = pd.read_csv("Housing.csv")

    with open("EXAMPLE.md", "w") as file:
        for _ in range(num_samples):
            # Sample a random entry from the dataset
            random_entry = housing_data.sample().iloc[0]

            # Extract relevant parameters
            price = random_entry['price']
            area = random_entry['area']
            bedrooms = random_entry['bedrooms']
            bathrooms = random_entry['bathrooms']

            sample_text = generate_real_estate_post(price, area, bedrooms, bathrooms)

            file.write(f"price={price}\narea={area}\nbedrooms={bedrooms}\nbathrooms={bathrooms}\n")
            file.write(sample_text + "\n------------------------ // divider\n")


if __name__ == "__main__":
    generate_and_save_samples()
