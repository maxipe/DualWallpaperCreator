from PIL import Image
import sys

def logError(errorMessage):
	print errorMessage
	
def getWallpaperSize(firstResolution, secondResolution, verticalOffset = 0):
	""" First and Second resolutions should be tuples
	with width and height. """
	return (firstResolution[0] + secondResolution[0],
		max(firstResolution[1],secondResolution[1] + verticalOffset) )

def openImage(imagePath):
	try:
		return Image.open(imagePath)
	except IOError:
		logError("\""+imagePath+"\""+" is not a valid image file.")
		
def createWallpaper(firstImagePath, secondImagePath, saveName, firstResolution, secondResolution, verticalOffset = 0):
	""" First and second images paths.
	Resolution of both screens	
	"""
	firstImage = openImage(firstImagePath)
	secondImage = openImage(secondImagePath)
	
	if (not firstImage) or (not secondImage):
		logError("Invalid image file. Stoped.")
		return

	#Resizing images to fit new one.	
	firstImage = firstImage.resize(firstResolution, Image.ANTIALIAS)
	secondImage = secondImage.resize(secondResolution, Image.ANTIALIAS)	

	wallpaperSize = getWallpaperSize(firstResolution, secondResolution, verticalOffset)

	newImage = Image.new('RGB', wallpaperSize)
	
	"""
	firstImagePixels = firstImage.load()
	secondImagePixels = secondImage.load()
	"""

	newImage.paste(firstImage,(0,0))
	newImage.paste(secondImage,(firstResolution[0],verticalOffset))
		
	newImage.save(saveName)

def main(arguments):
	firstResolution = (1920,1080)
	secondResolution = (1280,1024)
	verticalOffset = 0 #Second screen is N pixels below first screen
	
	if len(arguments) >= 3:
		firstImageName = arguments[1]
		secondImageName = arguments[2]
	else:
		firstImageName = "1.jpg"
		secondImageName = "2.jpg"

	saveName = "wallpaper.jpg"
	
	createWallpaper(firstImageName, secondImageName, saveName, firstResolution, secondResolution, verticalOffset)
	
if __name__ == "__main__":
	main(sys.argv)
		
else:
	pass
	#ToDo
