import uuid
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from module.utils.text_variables import ( 
    ZATYCHKA, 
    ACTION,
    CHOOSE_DELETE_TYPE,
    TODAYS_ACTIONS,
    UNDONED_ACTIONS,
    ACTION_ADDED 
)
from module.models.todos import User, ToDo


def action(update, context):
    """ Add inline keyboard """
    user = User.get(user_id=update.message.from_user.id)
    buttons = [
        [
            InlineKeyboardButton(text="add action", callback_data="action_add"),
            InlineKeyboardButton(text="delete action", callback_data="action_delete"),
            # InlineKeyboardButton(text="close this buttons", callback_data="action_close")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    context.bot.send_message(chat_id=user.user_id, text=ACTION, reply_markup=keyboard)


def keyboard_button_choice(update, context):
    """ InlineKeyboardButtons behavior """
    cb_query = update.callback_query
    cb_query_data = cb_query.data.split("_")[1]
    if cb_query_data == "add":
        return
        # user_data[update.callback_query.from_user.id] = user_value + 1
        # update_num_text(update.callback_query.message, user_value + 1)
    elif cb_query_data == "delete":
        user = User.get(user_id=cb_query.message.from_user.id)
        buttons = [
            [
                InlineKeyboardButton(text="today's", callback_data="date_today"),
                InlineKeyboardButton(text="tomorrow's", callback_data="date_tomorrow")
            ],
            InlineKeyboardButton(text="others", callback_data="date_others")
        ]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        context.bot.edit_text(chat_id=user.user_id, text=CHOOSE_DELETE_TYPE, reply_markup=keyboard)
    elif cb_query_data in ("today", "tomorrow", "others"):
        user = User.get(user_id=cb_query.message.from_user.id)
        date_dict = {
            "today": 1,
            "tomorrow": 2,
            "others": 3
        }
        query = ToDo.select().where((ToDo.user_id == user.user_id) & (ToDo.to_do_at_day == date_dict[cb_query_data]))
        actions_data = query.execute()
        inline_buttons = [
            InlineKeyboardButton(text=i.action, callback_data=str(i.action_id)) for i in actions_data
        ]
        buttons = [inline_buttons]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        context.bot.edit_text(chat_id=user.user_id, text=ZATYCHKA, reply_markup=keyboard)
    elif cb_query_data == "close":
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=cb_query.message.message_id)
    cb_query.answer()


def add_action(update, context):
    """ Add action's line to the database """
    user = User.get(user_id=update.message.from_user.id)
    text_message = ZATYCHKA
    buttons = []

    context.bot.send_message(
        chat_id=user.user_id,
        text=text_message,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=ZATYCHKA)], [InlineKeyboardButton(text=ZATYCHKA)]],
            one_time_keyboard=True,
            resize_keyboard=True)
    )
    #ToDo.create(
    #    user_id=update.message.from_user.id,
    #    defaults={'username': update.message.from_user.username, })

    context.bot.send_message(update.effective_chat.id, ACTION_ADDED)

    # ToDo.create(action_id='cvbnm', user_id='1-Qwerty', to_do_at_day='5', to_do_at_time='NULL',
    #             action='do english homework', description='NULL')


def delete_action(update, context):
    return


def ask_for_today(update, context):
    """ Showing today's actions """
    # -- add function to show actions for today
    context.bot.send_message(update.effective_chat.id, ZATYCHKA)


def ask_for_tomorrow(update, context):
    """ Showing tomorrow's actions """
    # -- add function to show actions for tomorrow
    context.bot.send_message(update.effective_chat.id, ZATYCHKA)


def ask_for_other(update, context):
    """ Showing all other's actions """
    # -- add function to show all other actions
    context.bot.send_message(update.effective_chat.id, ZATYCHKA)