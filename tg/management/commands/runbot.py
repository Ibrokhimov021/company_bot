from django.core.management.base import BaseCommand
from telegram.ext import (messagequeue as mq, Updater, CommandHandler, MessageHandler,ConversationHandler,
                            Filters, CallbackQueryHandler, CallbackContext)
from ...views import start
from ...mqbot import MQBot
from telegram.utils.request import Request



TOKEN = ''
class Command(BaseCommand):
    def handle(self, *args, **options):
        q = mq.MessageQueue(all_burst_limit=30, all_time_limit_ms=1000, group_burst_limit=20, group_time_limit_ms=60000, exc_route=None, autostart=True)
        request = Request(con_pool_size=36, connect_timeout=5.0, read_timeout=5.0)
        test_bot = MQBot(TOKEN, request=request, mqueue=q)
        updater = Updater(bot=test_bot, use_context=True, workers=32)

        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start",start))
        
        updater.start_polling()
        updater.idle()


if __name__ ==  '__main__':
    main()  