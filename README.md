# chatty v2
Chatty Bot with Local Ollama and Hugging Face Support

---
# How to Use?

##Install Ollama

*For Linux*
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

*Other OS*
<a href="https://ollama.com">Ollama</a>

## Install Model
```bash
ollama pull tinyllama:1.1b
```

## make .env file
*for linux*
``` bash
touch .env
```

## prepare .env

```python
BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN"
HUGGINGFACEHUB_API_TOKEN="YOUR_HUGGING_FACE_ACCESS_TOKEN" # hf token btw
```

## run
```bash
python3 source/bot.py
```

----
**Thank You!**
