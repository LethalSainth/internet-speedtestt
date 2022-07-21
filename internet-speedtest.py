import speedtest

# initiailize the test variable
test = speedtest.Speedtest()

# Get list of available servers for speed test
test.get_servers()

# Get best server for the speed test
best = test.get_best_server()

# Print the chosen best server 
print(f"Found: {best['host']} located in {best['country']}")

print("Getting download speed(bits/s)...")
download_res = test.download()
print('Getting upload speed(bits/s)...')
upload_res = test.upload()

print(f"Download Speed: {download_res/1024/1024:.2f} Mb/s")
print(f"Upload Speed: {upload_res/1024/1024:.2f} Mb/s")


# I just discovered the f-strings (allows you to format
# a string  in much the same way that you would with str.format()) 
# and realized i can add text inside the curly brackets as far as it is a raw string