import asyncio
from driver.veez import user
from pyrogram.types import Message
from pyrogram import Client, filters
from config import BOT_USERNAME, SUDO_USERS
from driver.filters import command, other_filters
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from driver.decorators import authorized_users_only, sudo_users_only


@Client.on_message(
    command(["/userbotjoin", f"نضم", "انضم"]) & other_filters
)
@authorized_users_only
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invitelink = await c.export_chat_invite_link(chat_id)
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
            await user.join_chat(invitelink)
            return await user.send_message(chat_id, "✅ انضممت للمجموعة بنجاح")
    except UserAlreadyParticipant:
        return await user.send_message(chat_id, "🙂 قد انضممت بالمجموعة مسبقاً")


@Client.on_message(
    command(["/userbotleave", f"غادر", "ادر"]) & other_filters
)
@authorized_users_only
async def leave_chat(_, m: Message):
    chat_id = m.chat.id
    try:
        await user.leave_chat(chat_id)
        return await _.send_message(
            chat_id,
            "✅ غادر الحساب المساعد المجموعه بنجاح",
        )
    except UserNotParticipant:
        return await _.send_message(
            chat_id,
            "❌ غادر الحساب المساعد المجموعه مسبقاً",
        )


@Client.on_message(command(["/leaveall", f"مغادره"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    
    msg = await message.reply("جارِ مغادرة الحساب المساعد من كل المجموعات انتظر قليلاً")
    async for dialog in user.iter_dialogs():
        try:
            await user.leave_chat(dialog.chat.id)
            left += 1
            await msg.edit(
                f".... جارِ المغادرة من كل المجموعات\n\n✅ تمت المغادره من: {left} مجموعه.\n❌ فشلت المغادره من: {failed} مجموعه."
            )
        except BaseException:
            failed += 1
            await msg.edit(
                f".... جارِ المغادره من كل المجموعات\n\n✅ تمت المغادره من: {left} مجموعه.\n❌ فشلت المغادره من: {failed} مجموعه."
            )
        await asyncio.sleep(0.7)
    await msg.delete()
    await client.send_message(
        message.chat.id, f"✅ اكتملت عملية المغادره من: {left} مجموعه.\n❌ فشلت عملية المغادره من: {failed} مجموعه."
    )


@Client.on_message(filters.left_chat_member)
async def ubot_leave(c: Client, m: Message):
#    ass_id = (await user.get_me()).id
    bot_id = (await c.get_me()).id
    chat_id = m.chat.id
    left_member = m.left_chat_member
    if left_member.id == bot_id:
        await user.leave_chat(chat_id)
#    elif left_member.id == ass_id:
#        await c.leave_chat(chat_id)
