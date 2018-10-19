from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])

data = image.generate('1234')
image.write('1234', 'out.png')