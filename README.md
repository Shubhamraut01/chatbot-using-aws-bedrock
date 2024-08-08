
# Chat Playground using Amazon Bedrock and Streamlit

This project is a simple chat application built using Streamlit that interfaces with Amazon Bedrock's Anthropic Claude model to generate responses to user input. The application allows users to type a message and receive a generated response using the power of AI.

## Features

- **Real-time Chat**: Interact with an AI model to generate responses based on user input.
- **Streamlit Interface**: Provides an easy-to-use web interface for inputting text and viewing responses.
- **Amazon Bedrock Integration**: Leverages AWS's Bedrock service to invoke the Claude model for text generation.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **AWS Account**: You need an AWS account with access to the Bedrock service.
- **AWS CLI Configured**: Ensure that your AWS CLI is configured with the appropriate credentials and region (e.g., `us-east-1`).
- **Python 3.x**: This project is built with Python, so you'll need Python installed on your system.
- **Streamlit**: Install Streamlit using pip:
  ```bash
  pip install streamlit


## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials**:
   Ensure your AWS credentials are configured in your environment. You can do this by running:
   ```bash
   aws configure
   ```

## Usage

To run the application, execute the following command:

```bash
streamlit run app.py
```

This will launch a local web server, and you can interact with the chat interface in your browser.

## Code Explanation

- **generate_response(prompt)**: This function takes a user's input (`prompt`) and sends a request to the Anthropic Claude model using Amazon Bedrock. It returns the model's response text.
- **Streamlit Interface**: 
  - The user input is captured using `st.text_input`.
  - Upon pressing the "Send" button, the `generate_response` function is invoked, and the generated response is displayed.

## Error Handling

The function includes a try-except block to catch and print any errors during the API call to Bedrock.

## Future Enhancements

- **Error Logging**: Implement better error logging and handling.
- **Model Selection**: Allow users to choose from different models available in Bedrock.
- **Styling Improvements**: Enhance the UI/UX of the Streamlit app.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Anthropic Claude](https://www.anthropic.com/)

