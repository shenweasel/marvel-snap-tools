import snapota_commands

def main():
    
    snapurl = input("What is the Snap OTA URL this week? ")
    
    if "cloudfront.net" in snapurl:
        snapota_commands.getOtaCloudfront(snapurl)
    else:
        snapota_commands.getOtaMain(snapurl)
   
if __name__ == "__main__":
    main()