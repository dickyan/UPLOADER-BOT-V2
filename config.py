import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5787026511:AAHG1T5KXQW93bahTDDFziKF1SRRhORMAcs")
    
    API_ID = int(os.environ.get("API_ID", 29863579))
    
    API_HASH = os.environ.get("API_HASH", "393f4ddd5618759cd4124e146030e94c")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "858874410"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://flowmix1:akuudataudia@cluster0.ejxh7vh.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
