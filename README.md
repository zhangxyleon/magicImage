# magicImage

magicImage is a flask app to process different images. I built this application to learn opencv and  practice flask. You can access it here: http://zhangxyleon.pythonanywhere.com/



## Grayscale Images

Surprisingly there are
[many](https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale)
acceptable and reasonable ways to convert a color image into a
[grayscale](https://en.wikipedia.org/wiki/Grayscale) ("black and white") image.
The complexity of each method scales with the amount that method accommodates
for human perception. For example, a very naive method is to average red, green
and blue intensities. A slightly better (and very popular method) is to take a
weighted average giving higher priority to green: 

<p align="center"><img src="/tex/a954b221cf9264cf11fcf943891f27bb.svg?invert_in_darkmode&sanitize=true" align=middle width=232.67438535pt height=14.611878599999999pt/></p>

