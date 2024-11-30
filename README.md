# TikTok Username Availability Checker 🔍

A powerful and efficient Python tool for checking the availability of TikTok usernames. Features include random username generation, bulk checking from file, Discord webhook notifications, and detailed logging capabilities.

## ⚠️ Disclaimer

This tool is for educational purposes only. Please ensure you comply with TikTok's Terms of Service and API usage guidelines when using this tool. The authors are not responsible for any misuse or potential consequences.

## ✨ Features

- Check username availability on TikTok
- Generate random usernames with custom length
- Bulk check usernames from a text file
- Discord webhook integration for available username notifications
- Detailed logging system
- File-based results storage (available, taken, and banned usernames)
- User-friendly command-line interface
- File picker dialog for selecting username lists

## 🔧 Requirements

- Python 3.7+
- Required packages:
  - requests
  - discord-webhook
  - tkinter (usually comes with Python)

## 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/9de/tiktok-username-checker.git
cd tiktok-username-checker
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Configure settings:
   - Rename `settings.example.json` to `settings.json`
   - Update the settings according to your preferences

## ⚙️ Configuration

Create a `settings.json` file with the following structure:

```json
{
    "discordWebhook": {
        "enable": true,
        "url": "YOUR_WEBHOOK_URL",
        "username": "TikTok Checker",
        "avatarurl": "https://example.com/avatar.png",
        "hexcolor": "FF0000"
    },
    "printbanned": true,
    "printbad": true,
    "SaveBanned": true,
    "saveBad": true
}
```

### Settings Explanation:
- `discordWebhook.enable`: Enable/disable Discord notifications
- `discordWebhook.url`: Your Discord webhook URL
- `printbanned`: Show banned usernames in console
- `printbad`: Show taken usernames in console
- `SaveBanned`: Save banned usernames to file
- `saveBad`: Save taken usernames to file

## 🚀 Usage

Run the script:
```bash
python checker.py
```

### Options:
1. **Random Username Generator**
   - Enter desired username length
   - Specify number of usernames to check
   - Tool will generate and check random usernames

2. **Check from File**
   - Select a text file containing usernames
   - One username per line
   - Tool will check each username in the file

### Output Files:
- `available.txt`: Available usernames
- `taken.txt`: Taken usernames (if enabled)
- `banned.txt`: Banned usernames (if enabled)
- `checker.log`: Detailed operation logs

## 📝 Logging

The tool maintains detailed logs in `checker.log`, including:
- Timestamp for each operation
- Username check results
- Error messages
- API response information

## 🔒 Rate Limiting

To avoid detection and maintain stability:
- The tool uses realistic user agents
- Implements session management
- Handles request timeouts
- Catches and logs exceptions

## 🛠 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📃 License

Distributed under the MIT License. See `LICENSE` for more information.

## ✉️ Contact

Project Link: [https://github.com/9de/tiktok-username-checker](https://github.com/9de/tiktok-username-checker)

## 🙏 Acknowledgments

- Thanks to all contributors who have helped with the development
- Inspired by the need for efficient TikTok username availability checking
