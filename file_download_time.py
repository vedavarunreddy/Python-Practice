'''
A programme that tells you how long it took to download a file from the internet.
'''
import time

def download_time(size, internet_speed=10):
    MEGABYTE = 8
    megabits_size = size * MEGABYTE
    download_time = megabits_size / internet_speed
    print(f"It will take {download_time} seconds to download. Served hot! ")
    while download_time > 0:
        download_time = download_time - 1
        print(download_time,"seconds left")
        time.sleep(1)
    print("\nDownload complete")
        


file_size = int(input("What is your file size in megabytes?: "))
net_speed = int(input("Internet speed in megabits/second: "))

download_time(file_size, net_speed)