import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from .models import Passwor, Employees, Reports
from .models import About, Super

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

button = [
    ["📝Ro'yhatdan o'tish",
     "Profilga kirish"
     ]
   
]


def start(update, context):
    user = update.message.from_user
    context.bot.send_message(user.id, 'Assalomu alaykum ',
                             reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True),
                             parse_mode="HTML")