from timezonefinder import TimezoneFinder
from datetime import datetime
from dateutil.tz import tzlocal
from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from module.utils.text_variables import ACCEPT_PHONE, YOUR_LOCATION, WANNA_CHANGE_LOCATION, CHANGE_QUESTION, \
    SEND_LOCATION, CHANGED_LOCATION, SURE, CLOSE
from module.models.users import User


def ask_for_phone(update, context):
    """ """
    user = User.get(user_id=update.message.from_user.id)
    text_message = ACCEPT_PHONE

    context.bot.send_message(
        chat_id=user.user_id,
        text=text_message,
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton(text=ACCEPT_PHONE)], [KeyboardButton(text=CLOSE)]],
            one_time_keyboard=True,
            resize_keyboard=True)
    )


def ask_for_location(update, context):
    """ Enter /location command """
    user = User.get(user_id=update.message.from_user.id)
    text_message = YOUR_LOCATION + ' UTC+' + str(user.utc_offset) + ':00'

    context.bot.send_message(
        chat_id=user.user_id,
        text=text_message,
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton(text=WANNA_CHANGE_LOCATION)], [KeyboardButton(text=CLOSE)]],
            one_time_keyboard=True,
            resize_keyboard=True)
    )


def change_location(update, context):
    """ Give the chance to change the timezone to user """
    user = User.get(user_id=update.message.from_user.id)

    context.bot.send_message(update.effective_chat.id, SURE)

    context.bot.send_message(
        chat_id=user.user_id,
        text=CHANGE_QUESTION,
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton(text=SEND_LOCATION, request_location=True)], [KeyboardButton(text=CLOSE)]],
            one_time_keyboard=True,
            resize_keyboard=True)
    )


def receive_location(update, context):
    """ Receiving user's location """
    # user = User.get(user_id=update.message.from_user.id)

    lat, lon = update.message.location.latitude, update.message.location.longitude
    # user.latitude, user.longitude = lat, lon
    tz = TimezoneFinder().timezone_at(lng=lon, lat=lat)
    query = User.update(timezone=tz).where(User.user_id == update.message.from_user.id)
    query.execute()

    current_time = datetime.now(tzlocal())
    query = User.update(utc_offset=current_time.utcoffset().total_seconds() / 3600)\
        .where(User.user_id == update.message.from_user.id)
    query.execute()

    update.message.reply_text(
        CHANGED_LOCATION,
        reply_markup=ReplyKeyboardRemove(),
    )
