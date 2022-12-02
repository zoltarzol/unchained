import os, openai
from django.shortcuts import render
from .forms import InputForm
from dotenv import load_dotenv
from datetime import datetime
from .functions import call_api

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG")

messages = []
question = ""

# def chatbot_home(request):
#     form = InputForm(request.POST or None)
#     message = None

#     if request.method == "POST":
#         pass
#     elif request.method == "GET":
#         form = ChatBotForm()
#         return render(request,'chatbot/chatbot.html')
#     else:
#         pass

def chatbot(request):
    form = InputForm(request.POST or None)
    user_msg = None     
    logged_in_user = request.user
    
    if form.is_valid() :
        user_msg = form.cleaned_data['text_msg']     
        messages.append({user_msg : ""})
        form = InputForm()
        time = datetime.today().strftime('%H:%M')
        
        response = call_api(user_msg)
        
        normalized_user_message = user_msg.replace(" ", "").replace(",", "").replace(".", "").lower()
        normalized_bot_message = response.replace(" ", "").replace(",", "").replace(".", "").lower()[2:]
        form = InputForm()
        
        if normalized_user_message == normalized_bot_message:
            global user_prompt
            user_prompt += f"You: {user_msg}\nFriend:"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=user_prompt,
                temperature=0.2,
                max_tokens=300,
                stop=["You:"]
                )
            messages.append({'': response['choices'][0]['text']})
            user_prompt += response['choices'][0]['text']
            return render(request, "chatbot/chatbot.html", {'form': form, 'messages':messages, 'time': time})

        else:
            messages.append({"" : response})
            return render(request, "chatbot/chatbot.html", {'form': form, 'messages':messages, 'time': time})

    else:
        messages.clear()

    return render(request, "chatbot/chatbot.html", {'form': form, 'messages':messages, 'user_name': logged_in_user})