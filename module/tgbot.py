import logging
from telegram.ext import Updater
from module.settings import TELEGRAM_TOKEN
# from module.utils.database_helper import DBConnection
from module.dispatcher import setup_dispatcher

# Setup bot handlers (you can see functions in dispatcher.py)
updater = Updater(TELEGRAM_TOKEN)
dp = updater.dispatcher
dp = setup_dispatcher(dp)

# Setup logging config type
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# def log_params(method_name, update):
#     logger.debug("Method: %s\nFrom: %s\nchat_id: %d\nText: %s" %
#                 (method_name,
#                  update.message.from_user,
#                  update.message.chat_id,
#                  update.message.text))

# Create database tables
from module.utils.database_helper import create_tables
create_tables()

# Run bot
updater.start_polling()
updater.idle()

# Close database connection
from module.utils.database_helper import db
if not updater.running and db:
    db.close()

