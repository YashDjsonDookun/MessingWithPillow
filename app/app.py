# Just playing with Python Pillow

import PIL.Image
import PIL.ImageFilter
import numpy as np

original_image = PIL.Image.open(r"{put your image path here}")
arr = np.asarray(original_image)

imageOne = PIL.Image.fromarray(arr)

black_white_ImageOne = imageOne.convert("L")
black_white_ImageOne.save(r"Images/after/{put your image path here}")

blurredImage_One = imageOne.filter(PIL.ImageFilter.BLUR)
blurredImage_One.save(r"Images/after/{put your image path here}")

gaussian_blurredImage_One = imageOne.filter(PIL.ImageFilter.GaussianBlur(15))
gaussian_blurredImage_One.save(r"Images/after/{put your image path here}")

minFilterImage_one = imageOne.filter(PIL.ImageFilter.MinFilter(3))  # max value here is 15
minFilterImage_one.save(r"Images/after/{put your image path here}")

maxFilterImage_one = imageOne.filter(PIL.ImageFilter.MaxFilter(3))  # max value here is 15
maxFilterImage_one.save(r"Images/after/{put your image path here}")

contourImage_one = imageOne.filter(PIL.ImageFilter.CONTOUR)
contourImage_one.save(r"Images/after/{put your image path here}")

embossImage_one = imageOne.filter(PIL.ImageFilter.EMBOSS)
embossImage_one.save(r"Images/after/{put your image path here}")

edgeEnhanceImage_one = imageOne.filter(PIL.ImageFilter.EDGE_ENHANCE)
edgeEnhanceImage_one.save(r"Images/after/{put your image path here}")

edgeMoreEnhanceImage_one = imageOne.filter(PIL.ImageFilter.EDGE_ENHANCE_MORE)
edgeMoreEnhanceImage_one.save(r"Images/after/{put your image path here}")

detailImage_one = imageOne.filter(PIL.ImageFilter.DETAIL)
detailImage_one.save(r"Images/after/{put your image path here}")

sharpenedImage_one = imageOne.filter(PIL.ImageFilter.SHARPEN)
sharpenedImage_one.save(r"Images/after/{put your image path here}")

sharpenedImage_one = imageOne.filter(PIL.ImageFilter.SHARPEN)
sharpenedImage_one.save(r"Images/after/{put your image path here}")

findEdgesImage_one = imageOne.filter(PIL.ImageFilter.FIND_EDGES)
findEdgesImage_one.save(r"Images/after/{put your image path here}")

smoothImage_one = imageOne.filter(PIL.ImageFilter.SMOOTH)
smoothImage_one.save(r"Images/after/{put your image path here}")

smoothMoreImage_one = imageOne.filter(PIL.ImageFilter.SMOOTH_MORE)
smoothMoreImage_one.save(r"Images/after/{put your image path here}")