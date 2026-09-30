# Automated Copywriting & Tone Transformer

## DecodeLabs Generative AI Training - Project 2

### Project Objective

The Automated Copywriting & Tone Transformer is a Python-based
application that generates marketing copy from a raw product
description.

The generated content is customized according to the selected
platform and tone.

### User Inputs

The application accepts:

- Product Name
- Platform
- Tone
- Product Description
- Temperature
- Top_P

### Supported Platforms

- LinkedIn
- Instagram
- Email

### Supported Tones

- Professional
- Friendly
- Exciting

### How It Works

1. The user enters the product name.
2. The user selects a target platform.
3. The user selects a tone.
4. The user enters the product description.
5. These values are inserted into a dynamic prompt template.
6. The prompt is sent to the generative AI model.
7. Temperature and Top_P control the generation parameters.
8. The generated marketing copy is displayed to the user.

### Technologies Used

- Python
- OpenAI API
- OpenAI Python SDK
- python-dotenv

### Project Structure

Automated-Copywriting-Tone-Transformer/
│
├── copywriter.py
├── README.md
├── .env
└── .gitignore

### Security

The API key is stored in a `.env` file and the `.env` file is
excluded from GitHub using `.gitignore`.

### Current Testing Status

The application successfully accepts all required user inputs
and reaches the OpenAI API request.

Live AI-generated output could not be completed during testing
because the API account had no remaining credits.

### Project Requirements Covered

- Dynamic prompt template
- User-defined Product Name
- User-defined Platform
- User-defined Tone
- Temperature parameter
- Top_P parameter
- Generative text generation