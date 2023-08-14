# requires: hikka-filters>=0.2.0

from .. import loader, utils
import re
from telethon.tl.functions.messages import StartBotRequest
@loader.tds
class TestModule(loader.Module):
    """Test module"""

    strings = {
        "name": "TestHikkaModule"
    }
    CHAT_ID = -1502641349
    bot_username = 'stupidwallet_bot'
    @loader.watcher() 
    async def watcher(self, message):
        pattern = r'https://t.me/stupidwallet_bot\?[^ ]+'
        message_text = ''
        if message.reply_markup:
            if message.reply_markup.rows:
                for row in message.reply_markup.rows:
                    for button in row.buttons:
                        if hasattr(button, 'url'):
                            button_url = button.url
                            message_text = button_url
        else:
            message_text = message.message

        matches = re.findall(pattern, message_text)
        for match in matches:
            start_parameter = match
            start_value = start_parameter.split('=')[1]
            print(f"Found start parameter in message: {start_parameter, start_value}")
            request = StartBotRequest("stupidwallet_bot", "stupidwallet_bot", start_value)
            result = await self._client(request)