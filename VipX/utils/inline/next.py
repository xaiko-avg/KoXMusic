
from typing import Union
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def next_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settings_back_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
        InlineKeyboardButton(
            text="★ 𝐍𝐄𝐗𝐓 ★", callback_data="settings_back_helper"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="❥𝐀𝐝𝐦𝐢𝐧❥",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="❦𝐀𝐮𝐭𝐡❦",
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="♡𝐛𝐥𝐚𝐜𝐤♡",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❣𝐆𝐜𝐚𝐬𝐭❣",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="❦𝐆𝐛𝐚𝐧❦",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="➳𝐋𝐲𝐫𝐢𝐜𝐬➳",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❦𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭🎙",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="𝐕𝐚𝐢𝐜𝐞ღ𝐂𝐡𝐚𝐭",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="♡𝐏𝐥𝐚𝐲♡",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="☙𝐒𝐮𝐝𝐨☙",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚜𝐒𝐓𝐀𝐑𝐓⚜",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def next_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="★ 𝐍𝐄𝐗𝐓 ★", callback_data="settings_back_helper"
                )

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎭 𝐇𝐄𝐋𝐏 🎭",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
