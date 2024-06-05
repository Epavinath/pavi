import turtle 
turtle.color('bisque')
turtle.bgcolor("maroon")
style = ('Courier', 30, 'normal')
turtle.write('AI_INNOVATIVE FOR _😎CHATBOT_😎', font=style, align='center')
turtle.hideturtle()

#user
User=["who are you",
      "you",
      "emoji",
      "i love you",
      "zombie",
      "lion",
      "who is your owner",
      "i like you",
      "hello",
      "What is the use of antivirus?",
      "how many players play cricket",
      "what is the eligible age for voting",
      "who is Abdul Kalam",
      "what are the scopes of cybersecurity in the future",
      "what is meant by an expert system",
      "define AI",
      "tell me about yourself",
      "Who created you",
      "i am also fine",
      "where is paavai engineering college",
      "what are your hobbies",
      "Are you married",
      "how old are you",
      "hi",
      "how are you",
      "Are you a robot?",
      "what is your name"]
#Bot replay
Bot=["I'M Lucifer😇",
     "🫵🏻",
     "There are different types of emoji there,😀😃😄😆🥹😅😂🤣🥲☺😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🥸🤩🥳😏😒😞😔😟😕🙁😤😭😠😡🤬🤯😳🥵🥶😶‍🌫️😱😨🫥🫤🫡🫢🤭😴🥱😲😮‍💨🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿👹",
     "Same to you 🫶🏻",
     "🧛🏻‍♀️🧛🏻🧛🏻‍♂️",
     "🦁Lion is wild animal🦁,KinG of Forest", 
     "🦁Pavi and Thiva are my owner🦁",
     "Me also 🥰",
     "Hello👋,How can i help you today🙋🏻‍♂️?",
     "Antivirus software is used to detect, prevent, and remove malicious software (malware) from computers and networks. It helps protect against viruses, worms, Trojans, and other types of malware that can harm computers and steal sensitive information",
     "🏏Cricket is typically played between two teams, with each team consisting of eleven players.",
     "The eligible age for voting varies by country. In many countries, including India, the eligible age for voting is 18 years old.",
     "Dr. APJ Abdul Kalam was an Indian scientist and politician who served as the 11th President of India from 2002 to 2007. He was known as the _Missile Man of India_ for his contributions to India's space and missile programs.",
     "🔐The future of cybersecurity holds opportunities in areas such as IoT security, cloud security, AI-powered cybersecurity, quantum cryptography, and threat intelligence🔑🔐",
     "An expert system is a computer system that emulates the decision-making ability of a human expert in a specific domain.It uses knowledge and inference rules to provide advice or make decisions.",
     "AI stands for Artificial Intelligence, which refers to the simulation of human intelligence processes by machines, especially computer systems.",
     "I'm an AI language model designed to assist with various tasks, from answering questions to generating text on a wide range of topics.",
     "I was developed by a team of researchers and engineers at PT",
     "Glad to hear that! Is there anything specific you'd like to talk about or any questions you have?",
     "Paavai Engineering College is located in Namakkal, Tamil Nadu, India. It's situated on the NH-7 Bypass Road, about 12 kilometers from Namakkal town.",
     "I don't have hobbies in the way humans do, but I enjoy processing information and learning about new topics.I'm here to assist with whatever you need!",
     "No i'm a robot 😲,like chatbot 🤖",
     "I'm 3 days old, What about you?",
     "HI👋,How can i help you today?",
     "I’m fine you",
     "Yes I am a robot, but I’m a good one. Let me prove it. How can I help you?",
     "I'm Lucifer :AI Developed by Pavinath,Thivagar (👬🏻)"]
for i in range(0,50):
    userwith=input("🤖Lucifer_AI🤖..")
    if (userwith in User):
        c=User.index(userwith)
        print(Bot[c])
    else:
        print("😓SORRY I DON'T KNOW HAVE ANSWER THIS QUESTION😓, (OR) 🤔IF YOU SPELLING MISTAKE CORRECT IT 🤔.")
