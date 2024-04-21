from Recall.backend.client import *
from Recall.backend.models.happening_formats import *
from Recall.backend.models.happenings import *
from Recall.backend.models.days import *

load_dotenv()
client = pymongo.MongoClient(os.getenv('uri'))

def main():
    ping()
    # add_format("Sleep quality", "Rating (1-5):")
