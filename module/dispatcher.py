"""
    Telegram event handlers
"""

from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from telegram import ReplyKeyboardRemove


from module.utils.text_variables import WELCOME_MESSAGE, DESCRIPTION_MESSAGE, WANNA_CHANGE_LOCATION, \
    DELETING_KEYBOARD, CLOSE
from module.models.users import User
# from module.todos import ToDo
# from module.dbhelper import DBConnection

from module.handlers.user_contacts import ask_for_location, change_location, receive_location
from module.handlers.actions import action, keyboard_button_choice, add_action, \
    ask_for_today, ask_for_tomorrow, ask_for_other


# basic commands functions
def start(update, context):
    """ Sending start message """
    context.bot.send_message(update.effective_chat.id, WELCOME_MESSAGE)
    context.bot.send_message(update.effective_chat.id, DESCRIPTION_MESSAGE)
    User.get_or_create(
        user_id=update.message.from_user.id,
        defaults={'username': update.message.from_user.username})


def help_message(update, context):
    """ Sending /help message """
    context.bot.send_message(update.effective_chat.id, DESCRIPTION_MESSAGE)


def info_message(update, context):
    """ Sending /info message """
    context.bot.send_message(update.effective_chat.id, DESCRIPTION_MESSAGE)


def close_reply_keyboard(update, context):
    deleting_message = update.message.reply_text(
        DELETING_KEYBOARD,
        reply_markup=ReplyKeyboardRemove(),
    )
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=deleting_message.message_id)


def setup_dispatcher(dp):
    """ Adding handlers for events from Telegram """

    # basic commands
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help_message))
    dp.add_handler(CommandHandler('info', info_message))

    dp.add_handler(MessageHandler(Filters.text([CLOSE]), close_reply_keyboard))

    # location changing
    dp.add_handler(CommandHandler('location', ask_for_location))
    dp.add_handler(MessageHandler(Filters.text([WANNA_CHANGE_LOCATION]), change_location))
    dp.add_handler(MessageHandler(Filters.location, receive_location))

    # to-do's actions
    dp.add_handler(CommandHandler('action', action))
    dp.add_handler(CallbackQueryHandler(keyboard_button_choice))
    # dp.add_handler(CommandHandler('add_action', add_action))

    dp.add_handler(CommandHandler('today', ask_for_today))
    dp.add_handler(CommandHandler('tomorrow', ask_for_tomorrow))
    dp.add_handler(CommandHandler('other', ask_for_other))

    return dp
