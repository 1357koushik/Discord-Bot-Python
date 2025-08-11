 Discord-Bot-Python

Replica of my 2021 discord bot code


> -  Pixel Bot



Pixel Bot is a Discord bot created using python level system using sql.



> -  Features



\-   **Welcome and Leave Messages:** Automatically sends a custom welcome message with a generated image when a new member joins and a leave message when a member leaves.

\-   **Leveling System:** Users can gain experience points (XP) by sending messages, which contributes to their level. The bot announces level-ups in a designated channel.

\-   **Art Showcase:** Provides a command for users to submit art, which is then posted in a specified channel with reaction emojis for voting.

\-   **Server Status:** Connects to a game server (likely a Bombsquad server via Telnet) to display a list of online players in a Discord channel.

\-   **General Commands: **

<img width="585" height="345.5" alt="image" src="https://github.com/user-attachments/assets/6f73289c-2fb8-40b3-a5ab-24da43240790" />
<img width="585" height="336.5" alt="image" src="https://github.com/user-attachments/assets/60c71526-0ef1-4e62-94de-4a39c3be2924" />


> -  Commands



> -  User Commands



\-   `-help`: Displays a list of all available commands.

\-   `-say \[message]`: Makes the bot repeat a message.

\-   `-avatar \[user\_id]`: Displays the avatar of a specified user. If no user ID is provided, it shows the author's avatar.

\-   `-level`: Shows the user's current level, XP, and rank within the server.

\-   `-ping`: Displays the bot's latency, CPU usage, and RAM usage.

\-   `-invite`: Provides a link to invite the bot to a server.

\-   `-sendart` or `-sa` `\[image\_url]`: Submits an image to the designated art channel for community voting.



> -  Admin Commands



These commands require administrator permissions to use.



\-   `-setwelmsg \[channel\_id]`: Sets the channel where welcome messages will be sent.

\-   `-setlevmsg \[channel\_id]`: Sets the channel where leave messages will be sent.

\-   `-setlevel \[channel\_id]`: Sets the channel where level-up announcements will be sent.

\-   `-setsenart \[channel\_id]`: Sets the channel for art submissions.



> -  Dependencies



This bot requires the following Python libraries:



\-   `discord.py`: The main library for interacting with the Discord API.

\-   `Pillow` (`PIL`): Used for image manipulation to create welcome and level-up cards.

\-   `requests`: Used to download user avatars.

\-   `psutil`: Used to get system information for the `-ping` command.

\-   `telnetlib`: Used to connect and interact with a remote game server.

\-   `mysql.connector`: Used for MySQL database connectivity.

\-   `sqlite3`: Used for local database storage.

\-   `nest\_asyncio`: Used to run asynchronous code in environments that don't support it by default.



You will also need font files (`CaviarDreams.ttf`, `NEON LED Light 400.ttf`) and a background image (`bg.jpg`) in the same directory as the script for the welcome and level commands to work correctly.



> -  Setup



1\.  Install Dependencies:

&nbsp;   `pip install -r requirements.txt` (assuming a `requirements.txt` file is created with the above libraries)

2\.  Configure Environment:

&nbsp;   -   Replace `'your token'` with your actual Discord bot token.

&nbsp;   -   Ensure the `bg.jpg` and font files are in the same directory as the script.

&nbsp;   -   Configure the MySQL connection details in the `getm` function.

3\.  Run the Bot:

&nbsp;   `python your\_bot\_file.py`



\*Note: The script contains hardcoded channel IDs and a Telnet password.\*

