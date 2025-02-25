from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import os

# 🔹 Telegram API Credentials (Get yours from https://my.telegram.org)
API_ID = 25205675  # Your API ID
API_HASH = "bc0464f8cb30f0d8fe0453cbe62bd531"  # Your API Hash
PHONE_NUMBER = "+40729581023"  # Your Telegram phone number

# 🔹 Group username from the link
GROUP_USERNAME = "@shaormacudetoate"  # Public group username

# 🔹 Folder to save images
image_dir = r"C:\Users\uie78384\Downloads\Panou"
os.makedirs(image_dir, exist_ok=True)

# 🔹 Connect to Telegram
client = TelegramClient("session_name", API_ID, API_HASH)

async def main():
    await client.start(PHONE_NUMBER)  # Log in (only needed once)

    try:
        # 🔹 Join the Group Automatically
        print(f"📩 Attempting to join {GROUP_USERNAME}...")
        await client(JoinChannelRequest(GROUP_USERNAME))
        print(f"✅ Successfully joined {GROUP_USERNAME}")

        # 🔹 Get Group Entity
        chat = await client.get_entity(GROUP_USERNAME)
        print(f"🔍 Accessed Group: {chat.title}")

        # 🔹 Check and Download the Profile Picture
        if chat.photo:
            image_path = os.path.join(image_dir, f"{GROUP_USERNAME.strip('@')}.jpg")
            await client.download_profile_photo(chat, file=image_path)
            print(f"✅ Profile picture downloaded: {image_path}")
        else:
            print("⚠️ No profile picture found for this group.")

    except Exception as e:
        print(f"❌ Error: {e}")

    await client.disconnect()

# Run the script
with client:
    client.loop.run_until_complete(main())
