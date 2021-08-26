# Test hello.py for git tutorial
# Second comment TODO add shebang
# Author: Purple Polygon
# E-mail: hello@muertech.com


import Greet


name = input("Put name: ")
greeter = Greet.Greeting_class(name)


if '__name__' == '__main__':
	pass
else:
    greeter.greet()
