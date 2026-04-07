import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

def text_to_command(user_text):
    prompt = f"""
    Convert this into a Windows CMD command.
    Only return command, no explanation.

    Input: {user_text}
    """

    response = model.generate_content(prompt)
    return response.text.strip()