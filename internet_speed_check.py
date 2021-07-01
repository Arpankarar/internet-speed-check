import speedtest
speed = speedtest.Speedtest()
print(f"Download speed: {'{:.1f}'.format(speed.download()/1024/1024)}Mb/s")
print(f"Upload speed: {'{:.1f}'.format(speed.download()/1024/1024)}Mb/s")