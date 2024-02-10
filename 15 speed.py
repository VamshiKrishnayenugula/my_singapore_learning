import speedtest

d_speed = speedtest.Speedtest()
print(f'upload speed is :  {d_speed.download()/800000:.2f}mb')


up_speed = speedtest.Speedtest()
print(f'down load speed is :  {up_speed.upload()/8000000:.2f}mb')
