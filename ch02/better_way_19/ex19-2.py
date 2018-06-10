remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)


remainder(number=20, 7)

>>>
SyntaxError: non-keyword arg after keyword arg


remainder(20, number=7)

>>>
TypeError: remainder() got multiple values for argument 'number'
