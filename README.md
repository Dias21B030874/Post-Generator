# Post-Generator
a post generator for an Instagram real estate account using the OpenAI ChatGPT gpt3.5-turbo API

Questions
How to mimic the style of successful Instagram posts?
Mimicking the style of successful Instagram posts involves using engaging and concise language, focusing on visual appeal, and incorporating relevant hashtags. The language should be positive, aspirational, and highlight the unique features of the real estate property.

What prompt engineering techniques can improve quality?
Provide specific details: Include specific property details in the prompts, such as price, area, bedrooms, bathrooms, to generate more contextually relevant responses.

Experiment with temperature: Adjust the temperature parameter during API calls to control the randomness of the generated text. Higher temperature values (e.g., 0.8) result in more creative outputs, while lower values (e.g., 0.2) produce more focused and deterministic responses.

How to ensure the model doesn't invent extra features?
Carefully structure the prompts by explicitly specifying the required parameters and using a system message to guide the model's behavior. Additionally, post-process the generated text to filter out any invented or irrelevant features, ensuring that the content aligns with the provided parameters. Regularly review and refine prompts based on generated outputs to improve model performance.