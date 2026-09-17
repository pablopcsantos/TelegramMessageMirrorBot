# Telegram Message Mirror Bot 🔄

Automation script developed in Python using the Telethon library, designed to asynchronously mirror messages between Telegram channels and groups.

## 🚀 Features

*   **1-to-1 Mirroring:** Reads from a source and instantly sends to a destination.
*   **History Recovery:** If run from scratch, the bot copies the entire past history in chronological order.
*   **Persistent Memory:** If the computer is turned off, the bot records the last message read and restarts exactly where it left off.
*   **Forum (Topics) Support:** Identifies if the source group has topics/subgroups, automatically creates the same tabs in the destination group, and forwards the contents to the correct location.
*   **Native Anti-Ban:** Queue and delay system structured to mimic human behavior and respect Telegram's *Rate Limit*.

## ⚙️ Installation and Usage

1. Clone the repository to your computer.
2. Install the requirements using the command:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the `tg_msg_mirror_bot.py` file and enter your Telegram credentials (`API_ID`, `API_HASH`) obtained from the official my.telegram.org website.
4. Configure the `SOURCE_CHANNEL` and `DESTINATION_CHANNEL` variables with the corresponding @username or numeric ID.
5. Run the script:
   ```bash
   python tg_msg_mirror_bot.py
   ```

## 🔑 How to Get Your Credentials and IDs

For the bot to work properly, you will need to fill in some variables in the `tg_msg_mirror_bot.py` file. Follow the steps below to find this information:

### 1. Obtaining `API_ID` and `API_HASH`
These credentials identify your script to Telegram servers.
1. Go to the official developer portal: [my.telegram.org](https://my.telegram.org).
2. Log in using your phone number (including country code, e.g., `+123456...`) and the confirmation code received in your Telegram app.
3. Click on **API development tools**.
4. If it's your first time, fill out the form to create a new application (the name and platform can be anything, for example: *MyApp* and *Desktop*).
5. Copy the values shown on the screen: **`App api_id`** (a short number) and **`App api_hash`** (a long sequence of letters and numbers).

### 2. Obtaining `SOURCE_CHANNEL` and `DESTINATION_CHANNEL`
How you fill in these variables depends on the privacy settings of the channel or group.
*   **For PUBLIC Channels/Groups:**
    *   Simply use the invite link or page username.
    *   *How to place in code:* `SOURCE_CHANNEL = '@channel_name'` (Always in quotes and with the `@` symbol).
*   **For PRIVATE Channels/Groups:**
    *   Private channels do not have a `@username`. You will need the hidden **numeric ID**.
    *   Open [Telegram Web](https://web.telegram.org) in your desktop browser.
    *   Navigate to the desired channel or group.
    *   Look at your **browser's address bar**. You will see a URL similar to this: `https://web.telegram.org/a/#-1001234567890`.
    *   Copy the entire numeric sequence, **including the minus sign and the 100** (e.g., `-1001234567890`).
    *   *How to place in code:* `SOURCE_CHANNEL = -1001234567890` (Since it is an integer, **DO NOT use quotes**).

## 👤 Authorship and Development
Automation script independently developed by Pablo Phillipe Cândido dos Santos, designed for the continuous mirroring of messages between Telegram channels and groups. The tool allows for past history copying and real-time forwarding, supporting the automatic creation and routing of subgroups (forum topics) to ensure fidelity and organization in the destination.

The development included the use of generative artificial intelligence tools as an auxiliary resource in the development process, with the author retaining full responsibility for the conception, implementation, integration, and verification of the project.

**Lattes Curriculum:** http://lattes.cnpq.br/9500873674712528
