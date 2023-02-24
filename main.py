import ftplib

# Define the FTP server address and port
server = "ftp.example.com"
port = 21

# Define a list of directories to scan
directories = ["/", "/pub", "/docs", "/files"]

# Define a list of common filenames to look for
filenames = ["readme.txt", "index.html", "home.html", "welcome.html"]

# Define a list to store the found files
found_files = []

# Loop through each directory
for directory in directories:
    try:
        # Connect to the FTP server and login anonymously
        ftp = ftplib.FTP()
        ftp.connect(server, port)
        ftp.login()

        # Change to the current directory
        ftp.cwd(directory)

        # Loop through each filename
        for filename in filenames:
            # Check if the file exists
            if filename in ftp.nlst():
                # Add the file to the list of found files
                found_files.append(directory + "/" + filename)

        # Disconnect from the FTP server
        ftp.quit()

    except Exception as e:
        print("Error: " + str(e))

# Print the list of found files
if len(found_files) > 0:
    print("Found the following files:")
    for file in found_files:
        print(file)
else:
    print("No files found.")
