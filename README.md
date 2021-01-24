# magicImage

magicImage is a flask app to process different images. I built this application to learn opencv and  practice flask. You can access it here: http://zhangxyleon.pythonanywhere.com/



## Grayscale Images

Surprisingly there are
[many](https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale)
acceptable and reasonable ways to convert a color image into a
[grayscale](https://en.wikipedia.org/wiki/Grayscale) ("black and white") image.
For example, a very simple method is to average red, green
and blue intensities. A slightly better (and very popular method) is to take a
weighted average giving higher priority to green: 


i = 0.2126r + 0.7152g + 0.0722b


##Face detection

Face Detection using Haar Cascades from opencv.
https://github.com/opencv/opencv/tree/master/data/haarcascades
