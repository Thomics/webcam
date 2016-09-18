import time, os

count = 0

#name - name of the photo, num is the iteration
def take_photo(interval, name, num):
	print(name + " " + str(num))

	cur_dir = os.getcwd()

	os.system("fswebcam -r 640x480 --no-banner " + cur_dir + "/photos/" + name + str(num))
	time.sleep(interval)


while True:
	count = count + 1
	take_photo(3, 'boat', count)
