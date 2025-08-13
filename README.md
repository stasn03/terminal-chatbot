# Terminal Chatbot

A terminal-based chatbot powered by the Mistral language model, designed for seamless interaction within your command-line interface.

## Features

- **Interactive Terminal Interface**: Engage in real-time conversations directly within your terminal.  
- **Syntax Highlighting**: Enjoy color-coded responses for enhanced readability.  
- **Code Block Detection**: Automatically identifies and formats code snippets within conversations.  
- **Customizable Styling**: Easily adjust the appearance through configuration files. 

## Run With Docker

### Prerequisites
- MistralAI API key  (get one here: https://console.mistral.ai/home)

### Steps
1. Create a ```.env``` file in the project root directory. Add the key as follows:
```env
API_KEY=your_api_key_here
```

2. Build the image
```bash
docker build -t terminal-chatbot .
```

3. Run the container with your API key:
```bash
docker run --env-file .env -it terminal-chatbot
```


## Run Without Docker
### Prerequisites

- Python 3.10 or higher  
- MistralAI API key  (get one here: https://console.mistral.ai/home)


### Steps

1. Clone this repository:

```bash
git clone https://github.com/stasn03/terminal-chatbot.git
cd terminal-chatbot
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file in the project root directory. Add the key as follows:
```env
API_KEY=your_api_key_here
```

Run the following command in the terminal inside the project directory to run the app:
```bash
python cli.py
```

## Customization
Change ```config.json``` to best suit your style.<br>
### Documentation for styling
**User input:** https://python-prompt-toolkit.readthedocs.io/en/master/<br>
**AI response:** https://rich.readthedocs.io/en/stable/introduction.html
