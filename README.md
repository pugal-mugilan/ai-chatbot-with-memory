# AI Chatbot 

A conversational CLI chatbot built with Python and Google Gemini API.
Built as part of my AI engineering learning journey.

## Features
- Multi-turn conversation with memory
- Persistent memory across sessions (saved to JSON)
- Custom system prompt / personality
- Clean conversation history management

## Tech Stack
- Python 3.11
- Google Gemini API (gemini-2.5-flash)
- google-genai SDK

## Setup

1. Clone the repo
   git clone https://github.com/yourusername/ai-engineering-portfolio

2. Create and activate virtual environment
   python3.11 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Set your API key
   export GEMINI_API_KEY="your-key-here"

## Usage

Stage 1 — Single API call
   python stage1_hello.py

Stage 2 — Conversation loop
   python stage2_conversation.py

Stage 3 — Persistent memory + system prompt
   python stage3_memory.py

## Key Concepts Learned
- How LLM APIs work (messages, roles, tokens)
- Why LLMs are stateless and how to fake memory
- System prompts and prompt engineering
- Persistent memory using JSON
- Virtual environments and dependency management

## Next Project
Project 2 — RAG App (Retrieval Augmented Generation)
