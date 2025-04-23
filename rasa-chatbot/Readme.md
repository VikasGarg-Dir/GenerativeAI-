# 🤖 Rasa Chatbot - Personal Info Collector

A conversational AI chatbot built using the Rasa framework. This bot greets users, collects their age and phone number using forms, handles mood-based conversation, and replies to general greetings and goodbyes.

## 🚀 Features

- Greets and farewells users
- Collects user's age and phone number via a form
- Responds based on user mood (happy or sad)
- Answers bot-related challenges (e.g., "Are you a bot?")
- Rule-based and story-based conversation flow
- Handles free-text number input using entity extraction

## 📁 Project Structure

```
rasa-chatbot/
│
├── data/
│   ├── nlu.yml           # Intent examples
│   ├── rules.yml         # Rules for predictable flows
│   └── stories.yml       # Stories to train dialogue management
│
├── domain.yml            # Domain config: intents, entities, slots, forms, responses
├── config.yml            # NLU pipeline and policies configuration
├── actions/              # Custom actions (if any)
│   └── actions.py
├── models/               # Trained model files
├── requirements.txt      # Python dependencies
└── README.md             # Project description and usage
```

## 🔧 Setup Instructions

### 1. 📦 Clone the Repository

```bash
git clone https://github.com/yourusername/rasa-chatbot.git
cd rasa-chatbot
```

### 2. 🐍 Create & Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. 🛠 Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. 📚 Train the Model

```bash
rasa train
```

### 5. 🧪 Test the Bot in Terminal

```bash
rasa shell
```

### 6. 💬 Chat via Custom UI or Webhook (Optional)

To integrate with a web front-end or messaging channel:

```bash
rasa run --enable-api
```

## 💡 How It Works

### 🔍 Intent Recognition
Defined in `nlu.yml`, e.g., `greet`, `goodbye`, `questions`, `mood_great`, `bot_challenge`.

### 🧠 Dialogue Flow
- **Forms**: Used to collect structured data like age and phone number.
- **Rules**: Hardcoded responses like answering "Are you a bot?"
- **Stories**: More flexible interactions that define full conversational flows.

### 🎯 Entity Extraction
The entity `number` is used to recognize age and phone numbers from free-text input.

### 🗂 Form Logic
The `question_form` is activated on `greet` and asks:
- `utter_ask_age`
- `utter_ask_number`

All slot mappings are defined in `domain.yml`.