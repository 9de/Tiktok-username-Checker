import random
import json
import logging
from datetime import datetime
from pathlib import Path
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import tkinter as tk
from tkinter import filedialog

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('checker.log'),
        logging.StreamHandler()
    ]
)

class TikTokChecker:
    def __init__(self):
        self.settings = self._load_settings()
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        })

    def _load_settings(self) -> dict:
        """Load settings from settings.json file."""
        try:
            with open("settings.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error("settings.json file not found")
            raise SystemExit(1)
        except json.JSONDecodeError:
            logging.error("Invalid JSON in settings.json")
            raise SystemExit(1)

    def send_webhook(self, username: str) -> None:
        """Send notification to Discord webhook when available username is found."""
        if not self.settings["discordWebhook"]["enable"]:
            return

        webhook = DiscordWebhook(
            url=self.settings["discordWebhook"]["url"],
            username=self.settings["discordWebhook"]["username"],
            avatar_url=self.settings["discordWebhook"]["avatarurl"]
        )

        embed = DiscordEmbed(color=self.settings["discordWebhook"]["hexcolor"])
        embed.set_author(
            name='New TikTok Available Username',
            url=f'https://tiktok.com/@{username}',
            icon_url='https://a.top4top.io/p_2268fq9kj1.png'
        )
        embed.set_footer(text='TikTok Checker')
        embed.set_timestamp()
        embed.add_embed_field(name='Username:', value=username)
        embed.add_embed_field(name='Found At:', value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        embed.set_thumbnail(url="https://a.top4top.io/s_2268fq9kj1.png")

        webhook.add_embed(embed)
        webhook.execute()

    def check_username(self, username: str) -> None:
        """Check if a TikTok username is available."""
        if not username:
            return

        try:
            response = self.session.get(
                f"https://m.tiktok.com/node/share/user/@{username}",
                timeout=10
            )
            data = response.json()
            status_code = data.get("statusCode")

            if status_code == 10202:  # Available username
                logging.info(f"[AVAILABLE] {username}")
                self.save_result("available.txt", username)
                self.send_webhook(username)
            elif status_code == 10221 and self.settings["printbanned"]:  # Banned username
                logging.info(f"[BANNED] {username}")
                if self.settings["SaveBanned"]:
                    self.save_result("banned.txt", username)
            elif status_code in {0, 10222, 10223, 10000} and self.settings["printbad"]:  # Taken username
                logging.info(f"[TAKEN] {username}")
                if self.settings["saveBad"]:
                    self.save_result("taken.txt", username)
            else:
                logging.warning(f"Unknown status code {status_code} for username: {username}")

        except requests.RequestException as e:
            logging.error(f"Error checking username {username}: {str(e)}")
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON response for username {username}")

    @staticmethod
    def save_result(filename: str, username: str) -> None:
        """Save username to specified file."""
        with open(filename, 'a') as f:
            f.write(f"{username}\n")

    @staticmethod
    def generate_username(length: int) -> str:
        """Generate random username of specified length."""
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789_'
        return ''.join(random.choice(chars) for _ in range(length))

def main():
    checker = TikTokChecker()
    
    print("\nTikTok Username Checker")
    print("[1] Random Username Generator")
    print("[2] Check from File")
    
    try:
        choice = int(input("\nSelect option: "))
        
        if choice == 1:
            length = int(input("Username length: "))
            count = int(input("Number of usernames to check: "))
            
            for _ in range(count):
                username = checker.generate_username(length)
                checker.check_username(username)
                
        elif choice == 2:
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(
                title="Select username file",
                filetypes=[("Text files", "*.txt")]
            )
            
            if file_path:
                with open(file_path, 'r') as f:
                    usernames = [line.strip() for line in f if line.strip()]
                
                for username in usernames:
                    checker.check_username(username)
            else:
                logging.error("No file selected")
                
        else:
            logging.error("Invalid option selected")
            
    except ValueError:
        logging.error("Please enter valid numbers")
    except KeyboardInterrupt:
        logging.info("Checker stopped by user")
    finally:
        input("\nPress Enter to exit...")

if __name__ == '__main__':
    main()
