import streamlit as st
import boto3
import json
# from botocore.exceptions import ClientError


client = boto3.client('bedrock-runtime','us-east-1')


def generate_response(prompt):
    native_request = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 512,
    "temperature": 0.5,
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt}],
        }
    ],
}
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    request = json.dumps(native_request)
    try: 
        response = client.invoke_model(
            modelId=model_id, body=request
        )
        print("response:::",response)
        # result = json.loads(response['body'].read())
        manas = json.loads(response.get('body').read())

        return manas["content"][0]["text"]
    except Exception as e:
        print(e)



st.title("Chat Playground using Amazon Bedrock and Streamlit")
# st.write("Type a message and get a response from the model.")


user_input = st.text_input("You: ")

if st.button("Send"):
    if user_input:
        response = generate_response(user_input)
        st.write(f" 💬 : {response}")
    else:
        st.write("Please enter a message.")