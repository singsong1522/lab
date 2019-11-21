def variable_arguement(fix1, fix2, *args):
    print('fix1={}, fix2={}'.format(fix1, fix2))
    for arg in args:
        print('variable part:{}'.format(arg))
variable_arguement("hello",'world')
variable_arguement('hi','again',300)
variable_arguement("it's me",'again',300,3.14,None)
variable_arguement("it\'s me",'again',300,3.14,None) #同樣效果

fruits = ['apple','banana','orange']
variable_arguement('buy some','fruits',fruits)
variable_arguement('buy some','fruits',*fruits)