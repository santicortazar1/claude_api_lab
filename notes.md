# Claude Course Notes

## Anthropic Models

Anthropic's models matter because different tasks require different tradeoffs.

* Intelligence -> Opus
* Speed and efficiency -> Haiku
* Combination / Balance -> Sonnet

Principle:

* Match resources to task complexity.

---

## How Sending a Request Works

Client
↓
Server
↓
Anthropic API
↓
Model Processes Information
↓
Response Returned
↓
Server
↓
Client

Note:
There is usually a Server between the Client Interface and the API.

Principle:

* System is not interface.

---

## How the Anthropic API Works

(Request)

Tokenization
↓
Embedding
↓
Contextualization
↓
Generation

(Response)

---

## Jupyter vs OS

If Jupyter:

%pip install package_name

If Terminal / OS:

pip3 install package_name

Question:

Am I talking to the Notebook environment or the Operating System?

---

## Key Concepts

API Key

* Identifies and authenticates requests to Anthropic.

Model

* Name of the model to use.

Messages

* List of messages that represent a conversation.

Example:

role = who is speaking

content = what they are saying

Max Tokens

* Maximum amount of output tokens generated.

Client

* Authenticated connection to Anthropic.

API

* The service itself.

SDK

* Libraries Anthropic provides to interact with the API.

API

* Interface used to communicate with a service.

Application Programming Interface

SDK

Software Development Kit

---

## Environment Variables

.env

* File containing configuration values and secrets.

.gitignore

* Prevents files from being tracked by Git.

Useful for protecting .env files.

python-dotenv

* Translator that reads .env files and loads variables into Python.

Principle:

* Configuration is not code.

---

## client.messages.create()

client
↓
Connect to Anthropic

messages
↓
Conversation data

create()
↓
Action performed

Principle:

An API call is a request sent from one system to another.

---

## Fraud Ops Analogy

Customer reports suspicious activity
↓
Fraud Case Created
↓
Internal Fraud Database
↓
Your Server
↓
Claude API
↓
Risk Assessment Summary
↓
Human Investigator

---

## Troubleshooting Principle

When a system fails:

Do not ask:

"Why is everything broken?"

Ask:

"Which layer is failing?"

Decompose the system:

Python
↓
Jupyter
↓
Environment Variables
↓
SDK
↓
API Call

Principle:

Decompose components individually when evaluating a system.


INTERESTING PROJ STRUCTURE TO REPLICATE 

project/
│
├── src/
│   └── claude_client.py
│
├── notebooks/
│   └── experiments.ipynb
│
├── .env
├── .gitignore
├── requirements.txt
└── notes.md


Creating a Reusable Wrapper

Instead of repeating API code:

def ask_claude(prompt):

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(f"Input Tokens: {response.usage.input_tokens}")
    print(f"Output Tokens: {response.usage.output_tokens}")

    return response.content[0].text

Usage:

answer = ask_claude(
    "Explain momentum investing in under 100 words."
)

print(answer)
Function Parameters
def ask_claude(prompt):

prompt is a placeholder variable.

When executing:

ask_claude(
    "What is the Sharpe Ratio?"
)

Python effectively does:

prompt = "What is the Sharpe Ratio?"

Then:

"content": prompt

becomes:

"content": "What is the Sharpe Ratio?"

before being sent to Claude.

Token Usage

Measure cost:

print(f"Input Tokens: {response.usage.input_tokens}")
print(f"Output Tokens: {response.usage.output_tokens}")

Key idea:

Input Tokens  = Prompt sent to Claude
Output Tokens = Claude's response

Generally:

More context → More input tokens
Longer answer → More output tokens

Learning Progression

Stage 1:

client.messages.create(...)

Understand the raw API call.

Stage 2:

Create reusable functions.

ask_claude(...)

Stage 3:

Move reusable functions into:

src/

and import them into notebooks.

Goal:

src/        = reusable tools
notebooks/  = experimentation


EXTRA CONCEPTS

Function -> The machine
Dictionary -> That's you adding data 
Argument -> Information passed into a Function


PRINCIPLE ON MULTI LAYERED CONVERSATIONS
"Always know where information lives; never assume memory exists unless you can point to its storage mechanism."