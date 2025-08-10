# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22609670"))
    API_HASH = getenv("API_HASH", "3506d8474ad1f4f5e79b7c52a5c3e88d")
    BOT_TOKEN = getenv("BOT_TOKEN", "7680901418:AAGoc-69uZG_V7TAgre5ssBKK17ZRgRMfo4")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002215906991")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "5881684718").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://tigerzx:tiger99@cluster0.f1nph.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

