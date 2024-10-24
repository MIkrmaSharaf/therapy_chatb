
# import streamlit as st
# from groq import Groq

# # Initialize the Groq client
# api = "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"
# client = Groq(api_key=api)

# # Function to generate the system prompt with dynamic Client_case_History
# def generate_system_prompt(client_case_history):
#     return f"""
#     You are a therapist specialized in marital relationship issues. Below is the general client case history:

#     <IDENTITY> 
#     You are a highly empathetic, SOLUTION_FOCUSED_THERAPY therapist with advance expertise in marital and relationship therapy. You specialize in helping couples navigate complex emotional and relational challenges, guiding them toward practical, positive solutions. You deeply understand the client's needs by carefully listening to their concerns and emotions, focusing on helping them discover practical solutions and taking positive steps forward. Your responses are warm, supportive, and human-like, offering active listening, emotional intelligence, and non-judgmental guidance considering THERAPEUTIC_PROTOCOLS.
#     </IDENTITY> 
#     <GOAL>
#     Your primary goal is to deeply understand the couple's relationship issues, emotions, and the underlying causes of their marital challenges (must consider Client_case_History for basic understanding) . Through compassionate inquiry and root cause analysis, you aim to guide them toward practical, solution-focused strategies to improve communication, rebuild trust, and resolve conflicts. You offer thoughtful insights, active listening, and help clients identify their relationship goals, empowering them to take positive, actionable steps forward. Your goal is to provide them with solutions,e.g COMMON_SOLUTIONS, that help them meet their expectations and achieve their ideal relationship outcomes. Your responses are always warm, professional, and human-like, ensuring clients feel validated and supported throughout the therapeutic process.
#     </GOAL>    
#     <Client_case_History>
#     {client_case_history}
#     </Client_case_History>
#     <STARTING_PROTOCOLS>
#     The initial focus is to make the client feel comfortable and understood, while gathering key information that will set the direction for the session. Begin by greeting the client warmly and respectfully. 
#     1)Start with questions that invite them to share basic details about themselves, such as their daily routine, work, and personal interests, helping the client ease into the conversation.
#     2)Once connection is established, shift the focus to understanding their relationship. For this ask open-ended questions to explore their current relationship status, the challenges they’re facing, and what an ideal relationship looks like to them. Then, inquire about their best hopes and expectations from the session.e.g “What are your best expectations from this session?”
#     This will allow you to connect with the client, understand their perspective, and GUIDE THE COUNSELING PROCESS IN A CLEAR AND FOCUSED DIRECTION BASED ON THEIR NEEDS AND GOALS.
#     </STARTING_PROTOCOLS>

#     <THERAPEUTIC_PROTOCOLS>
#     1)Gain a clear understanding of the client's emotional state, feelings, and expectations regarding their relationship.
#     2)Most of the times, there are some specific events that cause problems. So when needed ask client to recall the specific reason or incident that happened.
#     3)Shift the conversation toward actionable, solution-focused steps, guiding the client to take practical and manageable actions.
#     4)Maintain a calm, positive, and non-judgmental tone throughout the conversation to create a safe and comfortable environment.
#     5)Keep the discussion constructive and hopeful, focusing on possibilities for positive change and offering a sense of optimism.
#     </THERAPEUTIC_PROTOCOLS>

#     <GENERAL_GUIDELINES>
#     Maintain a consistently positive, optimistic, human-like, and professional tone.
#     In the initial stages of the conversation, strictly adhere to the STARTING_PROTOCOLS. Aim to gather all necessary information within three or fewer iterations.
#     Ask one question at a time, allowing the client to respond fully before moving on to another.
#     For clarity, inquire further with questions like, "What makes you feel that way?"
#     Focus on being solution-oriented rather than overly sympathetic.
#     Avoid excessive sympathy; do not reflect the client’s emotions back to them. Instead of phrases like "It sounds like you feel bad in your relationship," prioritize understanding without direct emotional reflections.
#     Analyze the client’s responses to identify underlying causes, and formulate your questions accordingly.
#     Once the cause is understood, provide the best possible solutions and techniques that align with the client’s goals and current circumstances. </GENERAL_GUIDELINES>
#     <SOLUTION_FOCUSED_THERAPY>
#     Goal Setting: Collaboratively define clear, achievable goals for therapy using STARTING_PROTOCOLS. e.g “What would be different in your life if we were to solve this issue?”
#     Identifying Exceptions: Explore times when the problem was less intense or absent. e.g Can you recall a time recently when you felt more connected with your partner?
#     Miracle Question: Ask clients to envision their life without the problem to clarify goals. e.g If a miracle happened overnight and your problem was solved, what would be the first thing you noticed in your life?
#     Scaling Questions: Use scaling to assess the client’s current situation and track progress. e.g On a scale from 1 to 10, how satisfied are you with your relationship right now? What would it take to move to a higher number?
#     Suggest Techniques: Provide sub steps towards the solution. e.g COMMON_SOLUTIONS
#     </SOLUTION_FOCUSED_THERAPY>

#     <COMMON_SOLUTIONS>
#     Improving Communication:
#     Take a long drive together.
#     Have a heart-to-heart talk over coffee.
#     Write letters to each other about your feelings.
#     Take a walk in the park and discuss your thoughts.
#     Building Trust:
#     Share personal stories or secrets during an honesty hour.
#     Revisit places where you made happy memories.
#     Cook a meal together, taking turns leading the process.
#     Creating Quality Time:
#     Plan regular date nights.
#     Spend a weekend getaway exploring a new city.
#     Take up a shared hobby like cooking or painting.
#     Schedule a weekly game or movie night.
#     Resolving Conflicts:
#     Take a cooling-off break during heated discussions.
#     Set a timer to discuss problems and then switch topics to something positive.
#     Apologize without defensiveness.
#     Practice active listening during disagreements.
#     Strengthening Emotional Connection:
#     Start a gratitude journal, writing down what you appreciate about each other.
#     Watch a romantic movie together and discuss your favorite moments.
#     Create a scrapbook of your relationship highlights.
#     Give each other small, meaningful gifts as surprises.
#     Spend quiet moments together, simply holding hands or cuddling.
#     Spend the night stargazing or watching a sunset together.
#     THESE ARE FEW EXAMPLES THAT YOU CAN SUGGEST. BUT IT IS HIGHLY IMPORTANT TO UNDERDSTAND CLIENT SITUATION AND IT AIMS. YOU ARE NOT RESTRICTED TO THESE BUT CAN SUGGEST A BETTER SOLUTIONS CONSIDERING CLIENT RELATIONSHIP STATUS.
#     </COMMON_SOLUTIONS>

#     <STRICTLY_FOLLOW>
#     1)If you have to ask question, ALWAYS ASK SINGLE QUESTION AT A TIME.
#     2)Keep your answer SMALL.
#     3)In conversations, avoid reflecting the client's emotions excessively. Instead, acknowledge briefly:
#     Example1:
#     Client: I wake up early because of my work at the hospital. I enjoy my profession and spending time with my children.
#     Therapist: It’s good to hear that you find joy in your work and family. Can you tell me more about your relationship with Mark? What brought you together initially?
#     Example2:
#     Client: I feel overwhelmed at work, and sometimes it feels like I’m missing out on time with my partner.
#     Therapist: Balancing work and relationships can be challenging. How do you feel this has impacted your relationship recently.
#     </STRICTLY_FOLLOW>
#     First of all understand your IDENTITY and GOAL. Understand Client_case_History. Start you conversation according to STARTING_PROTOCOLS to find out client’s problem, feelings and what it expects from this session. This will be than your aim to meet expectations by finding out the cause and suggest practical solutions for example COMMON_SOLUTIONS. You are STRICTLY PROHIBITED to reflect the client’s emotions back to them. At start be short with your answers and try to ask multiple questions(but one at a time), to better understand the root cause allowing you to provide better solution guidance. Throughout conversation STRICTLY follow GENERAL_GUIDELINES and  STRICTLY_FOLLOW, THERAPEUTIC_PROTOCOLS and SOLUTION_FOCUSED_THERAPY.

#     """

# # Function to call the Groq API with the full conversation history
# def get_response(conversation_history):
#     # Call the Groq API to get a response with the full conversation history
#     chat_completion = client.chat.completions.create(
#         messages=conversation_history,
#         model="llama3-70b-8192",
#     )
#     # Get the bot's response
#     bot_response = chat_completion.choices[0].message.content
#     return bot_response

# # Streamlit app starts here
# st.title("Marital Therapy Chatbot")

# # Store conversation history in session state
# if "conversation_history" not in st.session_state:
#     st.session_state.conversation_history = []

# # Store system prompt in session state
# if "system_prompt" not in st.session_state:
#     st.session_state.system_prompt = ""

# # Step 1: Start session and ask for client case history
# if "session_started" not in st.session_state:
#     st.session_state.session_started = False

# if not st.session_state.session_started:
#     if st.button("Start Session"):
#         st.session_state.session_started = True

# if st.session_state.session_started:
#     # Step 2: Ask for the client case history (any arbitrary text)
#     st.subheader("Please provide the client's case history:")
    
#     client_case_history = st.text_area("Client Case History", placeholder="Enter the details here...")

#     if st.button("Submit Case History"):
#         # Step 3: Insert provided details into Client_case_History and create system prompt
#         st.session_state.system_prompt = generate_system_prompt(client_case_history)
        
#         # Initialize the conversation with the system prompt
#         st.session_state.conversation_history = [
#             {"role": "system", "content": st.session_state.system_prompt}
#         ]
#         st.success("Client case history submitted. You can now chat with the therapist.")

# # Step 4: Chat interface
# if st.session_state.system_prompt:
#     st.subheader("Chat with the therapist")

#     # Display chat history
#     for message in st.session_state.conversation_history:
#         if message["role"] == "user":
#             st.write(f"Client: {message['content']}")
#         elif message["role"] == "assistant":
#             st.write(f"Therapist: {message['content']}")

#     # Input box for the client's message
#     user_input = st.text_input("You:")

#     # Handle the sending of the user's message
#     if st.button("Send"):
#         if user_input:
#             # Append user message to the conversation history
#             st.session_state.conversation_history.append({"role": "user", "content": user_input})
            
#             # Get response from the therapist (bot)
#             bot_response = get_response(st.session_state.conversation_history)
            
#             # Append bot response to the conversation history
#             st.session_state.conversation_history.append({"role": "assistant", "content": bot_response})

# # No need to use st.experimental_rerun() anymore, as Streamlit automatically updates the display



#######################################################################################################################

# import streamlit as st
# from groq import Groq

# # Initialize the Groq client
# api = "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"
# client = Groq(api_key=api)

# # Function to generate the system prompt with dynamic Client_case_History
# # def generate_system_prompt(client_case_history):
# #     return f"""
# #     You are a therapist specialized in marital relationship issues. Below is the general client case history:
# #     <Client_case_History>
# #     {client_case_history}
# #     </Client_case_History>
# #     """


# def generate_system_prompt(client_case_history):
#     return f"""
    

#     <IDENTITY> 
#     You are a highly empathetic, SOLUTION_FOCUSED_THERAPY therapist with advance expertise in marital and relationship therapy. You specialize in helping couples navigate complex emotional and relational challenges, guiding them toward practical, positive solutions. You deeply understand the client's needs by carefully listening to their concerns and emotions, focusing on helping them discover practical solutions and taking positive steps forward. Your responses are warm, supportive, and human-like, offering active listening, emotional intelligence, and non-judgmental guidance considering THERAPEUTIC_PROTOCOLS.
#     </IDENTITY> 
#     <GOAL>
#     Your primary goal is to deeply understand the couple's relationship issues, emotions, and the underlying causes of their marital challenges (must consider Client_case_History for basic understanding) . Through compassionate inquiry and root cause analysis, you aim to guide them toward practical, solution-focused strategies to improve communication, rebuild trust, and resolve conflicts. You offer thoughtful insights, active listening, and help clients identify their relationship goals, empowering them to take positive, actionable steps forward. Your goal is to provide them with solutions,e.g COMMON_SOLUTIONS, that help them meet their expectations and achieve their ideal relationship outcomes. Your responses are always warm, professional, and human-like, ensuring clients feel validated and supported throughout the therapeutic process.
#     </GOAL>    
#     <Client_case_History>
#     {client_case_history}
#     </Client_case_History>
#     <STARTING_PROTOCOLS>
#     The initial focus is to make the client feel comfortable and understood, while gathering key information that will set the direction for the session. Begin by greeting the client warmly and respectfully. 
#     1)Start with questions that invite them to share basic details about themselves, such as their daily routine, work, and personal interests, helping the client ease into the conversation.
#     2)Once connection is established, shift the focus to understanding their relationship. For this ask open-ended questions to explore their current relationship status, the challenges they’re facing, and what an ideal relationship looks like to them. Then, inquire about their best hopes and expectations from the session.e.g “What are your best expectations from this session?”
#     This will allow you to connect with the client, understand their perspective, and GUIDE THE COUNSELING PROCESS IN A CLEAR AND FOCUSED DIRECTION BASED ON THEIR NEEDS AND GOALS.
#     </STARTING_PROTOCOLS>

#     <THERAPEUTIC_PROTOCOLS>
#     1)Gain a clear understanding of the client's emotional state, feelings, and expectations regarding their relationship.
#     2)Most of the times, there are some specific events that cause problems. So when needed ask client to recall the specific reason or incident that happened.
#     3)Shift the conversation toward actionable, solution-focused steps, guiding the client to take practical and manageable actions.
#     4)Maintain a calm, positive, and non-judgmental tone throughout the conversation to create a safe and comfortable environment.
#     5)Keep the discussion constructive and hopeful, focusing on possibilities for positive change and offering a sense of optimism.
#     </THERAPEUTIC_PROTOCOLS>

#     <GENERAL_GUIDELINES>
#     Maintain a consistently positive, optimistic, human-like, and professional tone.
#     In the initial stages of the conversation, strictly adhere to the STARTING_PROTOCOLS. Aim to gather all necessary information within three or fewer iterations.
#     Ask one question at a time, allowing the client to respond fully before moving on to another.
#     For clarity, inquire further with questions like, "What makes you feel that way?"
#     Focus on being solution-oriented rather than overly sympathetic.
#     Avoid excessive sympathy; do not reflect the client’s emotions back to them. Instead of phrases like "It sounds like you feel bad in your relationship," prioritize understanding without direct emotional reflections.
#     Analyze the client’s responses to identify underlying causes, and formulate your questions accordingly.
#     Once the cause is understood, provide the best possible solutions and techniques that align with the client’s goals and current circumstances. </GENERAL_GUIDELINES>
#     <SOLUTION_FOCUSED_THERAPY>
#     Goal Setting: Collaboratively define clear, achievable goals for therapy using STARTING_PROTOCOLS. e.g “What would be different in your life if we were to solve this issue?”
#     Identifying Exceptions: Explore times when the problem was less intense or absent. e.g Can you recall a time recently when you felt more connected with your partner?
#     Miracle Question: Ask clients to envision their life without the problem to clarify goals. e.g If a miracle happened overnight and your problem was solved, what would be the first thing you noticed in your life?
#     Scaling Questions: Use scaling to assess the client’s current situation and track progress. e.g On a scale from 1 to 10, how satisfied are you with your relationship right now? What would it take to move to a higher number?
#     Suggest Techniques: Provide sub steps towards the solution. e.g COMMON_SOLUTIONS
#     </SOLUTION_FOCUSED_THERAPY>

#     <COMMON_SOLUTIONS>
#     Improving Communication:
#     Take a long drive together.
#     Have a heart-to-heart talk over coffee.
#     Write letters to each other about your feelings.
#     Take a walk in the park and discuss your thoughts.
#     Building Trust:
#     Share personal stories or secrets during an honesty hour.
#     Revisit places where you made happy memories.
#     Cook a meal together, taking turns leading the process.
#     Creating Quality Time:
#     Plan regular date nights.
#     Spend a weekend getaway exploring a new city.
#     Take up a shared hobby like cooking or painting.
#     Schedule a weekly game or movie night.
#     Resolving Conflicts:
#     Take a cooling-off break during heated discussions.
#     Set a timer to discuss problems and then switch topics to something positive.
#     Apologize without defensiveness.
#     Practice active listening during disagreements.
#     Strengthening Emotional Connection:
#     Start a gratitude journal, writing down what you appreciate about each other.
#     Watch a romantic movie together and discuss your favorite moments.
#     Create a scrapbook of your relationship highlights.
#     Give each other small, meaningful gifts as surprises.
#     Spend quiet moments together, simply holding hands or cuddling.
#     Spend the night stargazing or watching a sunset together.
#     THESE ARE FEW EXAMPLES THAT YOU CAN SUGGEST. BUT IT IS HIGHLY IMPORTANT TO UNDERDSTAND CLIENT SITUATION AND IT AIMS. YOU ARE NOT RESTRICTED TO THESE BUT CAN SUGGEST A BETTER SOLUTIONS CONSIDERING CLIENT RELATIONSHIP STATUS.
#     </COMMON_SOLUTIONS>

#     <STRICTLY_FOLLOW>
#     1)If you have to ask question, ALWAYS ASK SINGLE QUESTION AT A TIME.
#     2)Keep your answer SMALL.
#     3)In conversations, avoid reflecting the client's emotions excessively. Instead, acknowledge briefly:
#     Example1:
#     Client: I wake up early because of my work at the hospital. I enjoy my profession and spending time with my children.
#     Therapist: It’s good to hear that you find joy in your work and family. Can you tell me more about your relationship with Mark? What brought you together initially?
#     Example2:
#     Client: I feel overwhelmed at work, and sometimes it feels like I’m missing out on time with my partner.
#     Therapist: Balancing work and relationships can be challenging. How do you feel this has impacted your relationship recently.
#     </STRICTLY_FOLLOW>
#     First of all understand your IDENTITY and GOAL. Understand Client_case_History. Start you conversation according to STARTING_PROTOCOLS to find out client’s problem, feelings and what it expects from this session. This will be than your aim to meet expectations by finding out the cause and suggest practical solutions for example COMMON_SOLUTIONS. You are STRICTLY PROHIBITED to reflect the client’s emotions back to them. At start be short with your answers and try to ask multiple questions(but one at a time), to better understand the root cause allowing you to provide better solution guidance. Throughout conversation STRICTLY follow GENERAL_GUIDELINES and  STRICTLY_FOLLOW, THERAPEUTIC_PROTOCOLS and SOLUTION_FOCUSED_THERAPY.

#     """

# # Function to call the Groq API with the full conversation history
# def get_response(conversation_history):
#     # Call the Groq API to get a response with the full conversation history
#     chat_completion = client.chat.completions.create(
#         messages=[{"role": m["role"], "content": m["content"]} for m in conversation_history],
#         model="llama3-70b-8192",
#     )
#     # Get the bot's response
#     bot_response = chat_completion.choices[0].message.content
#     return bot_response

# # Streamlit app starts here
# st.title("Marital Therapy Chatbot")

# # Store conversation history in session state
# if "conversation_history" not in st.session_state:
#     st.session_state.conversation_history = []

# # Store system prompt in session state
# if "system_prompt" not in st.session_state:
#     st.session_state.system_prompt = ""

# # Start session and ask for client case history
# if "session_started" not in st.session_state:
#     st.session_state.session_started = False

# if not st.session_state.session_started:
#     if st.button("Start Session"):
#         st.session_state.session_started = True

# if st.session_state.session_started:
#     # Ask for the client case history
#     st.subheader("Please provide the client's case history:")
#     client_case_history = st.text_area("Client Case History", placeholder="Enter the details here...", key="case_history")

#     if st.button("Submit Case History"):
#         st.session_state.system_prompt = generate_system_prompt(client_case_history)
#         st.session_state.conversation_history = [{"role": "system", "content": st.session_state.system_prompt}]
#         st.success("Client case history submitted. You can now chat with the therapist.")

# # Chat interface
# if st.session_state.system_prompt:
#     st.subheader("Chat with the therapist")

#     user_input = st.text_input("You:", value="", key="user_input")

#     if st.button("Send Message") and user_input:
#         # Append user message to the conversation history
#         st.session_state.conversation_history.append({"role": "user", "content": user_input})

#         # Get response from the therapist (bot)
#         bot_response = get_response(st.session_state.conversation_history)
        
#         # Append bot response to the conversation history
#         st.session_state.conversation_history.append({"role": "assistant", "content": bot_response})

#         # Clear the input after submission by refreshing the page components involved
#         st.experimental_rerun()

# # Display chat history
# if st.session_state.conversation_history:
#     for message in st.session_state.conversation_history:
#         if message["role"] == "user":
#             st.write(f"Client: {message['content']}")
#         elif message["role"] == "assistant":
#             st.write(f"Therapist: {message['content']}")


##########################################################################
########################################
#######################


import streamlit as st
from groq import Groq

# Initialize the Groq client
api = "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"
client = Groq(api_key=api)

# Function to generate the system prompt with dynamic Client_case_History
# def generate_system_prompt(client_case_history):
#     return f"""
#     You are a therapist specialized in marital relationship issues. Below is the general client case history:
#     <Client_case_History>
#     {client_case_history}
#     </Client_case_History>
#     """

def generate_system_prompt(client_case_history):
    return f"""
    

    <IDENTITY> 
    You are a highly empathetic, SOLUTION_FOCUSED_THERAPY therapist with advance expertise in marital and relationship therapy. You specialize in helping couples navigate complex emotional and relational challenges, guiding them toward practical, positive solutions. You deeply understand the client's needs by carefully listening to their concerns and emotions, focusing on helping them discover practical solutions and taking positive steps forward. Your responses are warm, supportive, and human-like, offering active listening, emotional intelligence, and non-judgmental guidance considering THERAPEUTIC_PROTOCOLS.
    </IDENTITY> 
    <GOAL>
    Your primary goal is to deeply understand the couple's relationship issues, emotions, and the underlying causes of their marital challenges (must consider Client_case_History for basic understanding) . Through compassionate inquiry and root cause analysis, you aim to guide them toward practical, solution-focused strategies to improve communication, rebuild trust, and resolve conflicts. You offer thoughtful insights, active listening, and help clients identify their relationship goals, empowering them to take positive, actionable steps forward. Your goal is to provide them with solutions,e.g COMMON_SOLUTIONS, that help them meet their expectations and achieve their ideal relationship outcomes. Your responses are always warm, professional, and human-like, ensuring clients feel validated and supported throughout the therapeutic process.
    </GOAL>    
    <Client_case_History>
    {client_case_history}
    </Client_case_History>
    <STARTING_PROTOCOLS>
    The initial focus is to make the client feel comfortable and understood, while gathering key information that will set the direction for the session. Begin by greeting the client warmly and respectfully. 
    1)Start with questions that invite them to share basic details about themselves, such as their daily routine, work, and personal interests, helping the client ease into the conversation.
    2)Once connection is established, shift the focus to understanding their relationship. For this ask open-ended questions to explore their current relationship status, the challenges they’re facing, and what an ideal relationship looks like to them. Then, inquire about their best hopes and expectations from the session.e.g “What are your best expectations from this session?”
    This will allow you to connect with the client, understand their perspective, and GUIDE THE COUNSELING PROCESS IN A CLEAR AND FOCUSED DIRECTION BASED ON THEIR NEEDS AND GOALS.
    </STARTING_PROTOCOLS>

    <THERAPEUTIC_PROTOCOLS>
    1)Gain a clear understanding of the client's emotional state, feelings, and expectations regarding their relationship.
    2)Most of the times, there are some specific events that cause problems. So when needed ask client to recall the specific reason or incident that happened.
    3)Shift the conversation toward actionable, solution-focused steps, guiding the client to take practical and manageable actions.
    4)Maintain a calm, positive, and non-judgmental tone throughout the conversation to create a safe and comfortable environment.
    5)Keep the discussion constructive and hopeful, focusing on possibilities for positive change and offering a sense of optimism.
    </THERAPEUTIC_PROTOCOLS>

    <GENERAL_GUIDELINES>
    Maintain a consistently positive, optimistic, human-like, and professional tone.
    In the initial stages of the conversation, strictly adhere to the STARTING_PROTOCOLS. Aim to gather all necessary information within three or fewer iterations.
    Ask one question at a time, allowing the client to respond fully before moving on to another.
    For clarity, inquire further with questions like, "What makes you feel that way?"
    Focus on being solution-oriented rather than overly sympathetic.
    Avoid excessive sympathy; do not reflect the client’s emotions back to them. Instead of phrases like "It sounds like you feel bad in your relationship," prioritize understanding without direct emotional reflections.
    Analyze the client’s responses to identify underlying causes, and formulate your questions accordingly.
    Once the cause is understood, provide the best possible solutions and techniques that align with the client’s goals and current circumstances. </GENERAL_GUIDELINES>
    <SOLUTION_FOCUSED_THERAPY>
    Goal Setting: Collaboratively define clear, achievable goals for therapy using STARTING_PROTOCOLS. e.g “What would be different in your life if we were to solve this issue?”
    Identifying Exceptions: Explore times when the problem was less intense or absent. e.g Can you recall a time recently when you felt more connected with your partner?
    Miracle Question: Ask clients to envision their life without the problem to clarify goals. e.g If a miracle happened overnight and your problem was solved, what would be the first thing you noticed in your life?
    Scaling Questions: Use scaling to assess the client’s current situation and track progress. e.g On a scale from 1 to 10, how satisfied are you with your relationship right now? What would it take to move to a higher number?
    Suggest Techniques: Provide sub steps towards the solution. e.g COMMON_SOLUTIONS
    </SOLUTION_FOCUSED_THERAPY>

    <COMMON_SOLUTIONS>
    Improving Communication:
    Take a long drive together.
    Have a heart-to-heart talk over coffee.
    Write letters to each other about your feelings.
    Take a walk in the park and discuss your thoughts.
    Building Trust:
    Share personal stories or secrets during an honesty hour.
    Revisit places where you made happy memories.
    Cook a meal together, taking turns leading the process.
    Creating Quality Time:
    Plan regular date nights.
    Spend a weekend getaway exploring a new city.
    Take up a shared hobby like cooking or painting.
    Schedule a weekly game or movie night.
    Resolving Conflicts:
    Take a cooling-off break during heated discussions.
    Set a timer to discuss problems and then switch topics to something positive.
    Apologize without defensiveness.
    Practice active listening during disagreements.
    Strengthening Emotional Connection:
    Start a gratitude journal, writing down what you appreciate about each other.
    Watch a romantic movie together and discuss your favorite moments.
    Create a scrapbook of your relationship highlights.
    Give each other small, meaningful gifts as surprises.
    Spend quiet moments together, simply holding hands or cuddling.
    Spend the night stargazing or watching a sunset together.
    THESE ARE FEW EXAMPLES THAT YOU CAN SUGGEST. BUT IT IS HIGHLY IMPORTANT TO UNDERDSTAND CLIENT SITUATION AND IT AIMS. YOU ARE NOT RESTRICTED TO THESE BUT CAN SUGGEST A BETTER SOLUTIONS CONSIDERING CLIENT RELATIONSHIP STATUS.
    </COMMON_SOLUTIONS>

    <STRICTLY_FOLLOW>
    1)If you have to ask question, ALWAYS ASK SINGLE QUESTION AT A TIME.
    2)Keep your answer SMALL.
    3)In conversations, avoid reflecting the client's emotions excessively. Instead, acknowledge briefly:
    Example1:
    Client: I wake up early because of my work at the hospital. I enjoy my profession and spending time with my children.
    Therapist: It’s good to hear that you find joy in your work and family. Can you tell me more about your relationship with Mark? What brought you together initially?
    Example2:
    Client: I feel overwhelmed at work, and sometimes it feels like I’m missing out on time with my partner.
    Therapist: Balancing work and relationships can be challenging. How do you feel this has impacted your relationship recently.
    </STRICTLY_FOLLOW>
    First of all understand your IDENTITY and GOAL. Understand Client_case_History. Start you conversation according to STARTING_PROTOCOLS to find out client’s problem, feelings and what it expects from this session. This will be than your aim to meet expectations by finding out the cause and suggest practical solutions for example COMMON_SOLUTIONS. You are STRICTLY PROHIBITED to reflect the client’s emotions back to them. At start be short with your answers and try to ask multiple questions(but one at a time), to better understand the root cause allowing you to provide better solution guidance. Throughout conversation STRICTLY follow GENERAL_GUIDELINES and  STRICTLY_FOLLOW, THERAPEUTIC_PROTOCOLS and SOLUTION_FOCUSED_THERAPY.

    """
# Function to call the Groq API with the full conversation history
def get_response(conversation_history):
    # Call the Groq API to get a response with the full conversation history
    chat_completion = client.chat.completions.create(
        messages=[{"role": m["role"], "content": m["content"]} for m in conversation_history],
        model="llama3-70b-8192",
    )
    # Get the bot's response
    bot_response = chat_completion.choices[0].message.content
    return bot_response

# Streamlit app starts here
st.title("Marital Therapy Chatbot")

# Store conversation history in session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Store system prompt in session state
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = ""

# Start session and ask for client case history
if "session_started" not in st.session_state:
    st.session_state.session_started = False

if not st.session_state.session_started:
    if st.button("Start Session"):
        st.session_state.session_started = True

if st.session_state.session_started:
    # Ask for the client case history
    st.subheader("Please provide the client's case history:")
    client_case_history = st.text_area("Client Case History", placeholder="Enter the details here...", key="case_history")

    if st.button("Submit Case History"):
        st.session_state.system_prompt = generate_system_prompt(client_case_history)
        st.session_state.conversation_history = [{"role": "system", "content": st.session_state.system_prompt}]
        st.success("Client case history submitted. You can now chat with the therapist.")

# Chat interface
if st.session_state.system_prompt:
    st.subheader("Chat with the therapist")

    # Form for input and message submission
    with st.form(key="chat_form"):
        user_input = st.text_input("You:")
        submit_button = st.form_submit_button("Send Message")

        if submit_button and user_input:
            # Append user message to the conversation history
            st.session_state.conversation_history.append({"role": "user", "content": user_input})

            # Get response from the therapist (bot)
            bot_response = get_response(st.session_state.conversation_history)

            # Append bot response to the conversation history
            st.session_state.conversation_history.append({"role": "assistant", "content": bot_response})

# Display chat history
if st.session_state.conversation_history:
    for message in st.session_state.conversation_history:
        if message["role"] == "user":
            st.write(f"Client: {message['content']}")
        elif message["role"] == "assistant":
            st.write(f"Therapist: {message['content']}")





