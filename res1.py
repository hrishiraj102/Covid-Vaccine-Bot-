def sample_responses1(input_text):
    user_message = str(input_text).lower()
    
    if 'hi' in user_message:
        return 'Hi'
    if 'how are you' in user_message:
        return 'I am Good.Stay Home'
    if 'owner' in user_message:
        return 'Hrishiraj'