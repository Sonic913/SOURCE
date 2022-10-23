# Copyright (C) 2022 By Shadow

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from driver.decorators import sudo_users_only
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_PHOTO,
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("الصفحه الرئيسيه")
    await query.edit_message_text(
        f"""✨ **هَــْـْـْْـلاّ »「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」**\n
 **⌔︙انا بوت تشغيل الموسيقى في المكالمات المرئية 

⌔︙ لمعرفة اوامر البوت اضغط على » اوامر البوت

⌔︙ لمعرفة طريقة تشغيل البوت اضغط على » طريقة التشغيل
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✦ طريقة التشغيل ✦", callback_data="cbhowtouse"),
                    InlineKeyboardButton("✦ الحساب المساعد ✦", url=f"https://t.me/{ASSISTANT_NAME}"),
                    ],
                [
                    InlineKeyboardButton("✦ اوامر البوت ✦", callback_data="cbcmds"),
                    InlineKeyboardButton("✦ مطور البوت ✦", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "✦ مجموعة الدعم ✦", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "✦ قناة السورس ✦", url=f"https://t.me/SONIC_source"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "✦ اضف البـوت الى مجموعتك✦",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("طريقة التشغيل")
    await query.edit_message_text(
        f""" هذه طريقة تشغيل و تفعيل البوت:

 1 ↤ أولاً ، أضفني إلى مجموعتك
 2 ↤ بعد ذلك ، قم بترقيتي كمشرف ومنح جميع الصلاحيات باستثناء البقاء مخفياً
 3 ↤ بعد ترقيتي ، اكتب حدث في المجموعة لتحديث بيانات المشرفين
 4 ↤ أضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب انضم لدعوة حساب المساعد
 5 ↤ قم بفتح المكالمة  أولاً قبل البدء في تشغيل الموسيقى
 6 ↤ في بعض الأحيان ، يمكن أن تساعدك إعادة تحميل البوت باستخدام الأمر حدث في إصلاح بعض المشاكل
 📌 إذا لم ينضم البوت إلى المكالمة ، فتأكد من تشغيل المكالمة ، أو اكتب ادر ثم اكتب نضم مرة أخرى

 💡 إذا كانت لديك أسئلة  حول البوت ، فيمكنك إخبارنا منن خلال مجموعة الدعم الخاصة بي 

⚡ قناة البوت @{UPDATES_CHANNEL}
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("قائمة الاوامر")
    await query.edit_message_text(
        f"""» **قم بالضغط على الزر الذي تريده لمعرفه الاوامر الخاصه به  !**

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✦ اوامر المشرفين ✦", callback_data="cbadmin"),
                    InlineKeyboardButton("✦ اوامر المطور ✦", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("✦ اوامر اساسيه ✦", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("الاوامر الاساسيه")
    await query.edit_message_text(
        f"""🏮 الاوامر الاساسيه:

» تشغيل +「اسم الموسيقى / رابط」لتشغيل الموسيقى في المحادثه المرئيه
» القائمة 「تظهر لك قائمة التشغيل」
» انهاء「لإنهاء الموسيقى في المكالمه」
» تحميل + 「الاسم تنزيل صوت من اليوتيوب」
»نزل + 「الاسم  تنزيل فيديو من اليوتيوب」
» تخطي 「للتخطي إلى التالي」
» السرعه 「إظهار سرعة البوت」
⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("اوامر الادمنيه")
    await query.edit_message_text(
        f"""🏮  أوامر المشرفين:

» توقف 「ايقاف التشغيل موقتآ」
» اكمل 「استئناف التشغيل」
» ايقاف「لإيقاف التشغيل」
» /vmute 「لكتم البوت」
» /vunmute 「لرفع الكتم عن البوت」
» /volume 「ضبط مستوئ الصوت」
» /reload「لتحديث البوت و قائمة المشرفين」
» /userbotjoin「لاستدعاء الحساب المساعد」
» /userbotleave「لطرد الحساب المساعد」
⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
@sudo_users_only
async def cbsudo(_, query: CallbackQuery):
    await query.answer("اوامر المطور")
    await query.edit_message_text(
        f"""🏮 هنا اوامر المطور:

» /rmw「لحذف جميع الملفات 」
» /rmd「حذف جميع الملفات المحمله」
» /sysinfo「لمعرفه معلومات السيرفر」
» /update「لتحديث بوتك لاخر نسخه」
» /restart「اعاده تشغيل البوت」
» /leaveall「خروج الحساب المساعد من جميع المجموعات」

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المشرف الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر ", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المشرف الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر ", show_alert=True)
    await query.message.delete()
