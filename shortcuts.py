""" 10 Python Shortcuts You Need To Know
https://www.youtube.com/watch?v=CssrFJGH_dU"""
class Shortcuts:
    def __init__(self):
        pass

    def escape_quote_func(self):
        name = 'Quang'
        # x =print('hello I don\'t like single quote at all')
        x = f' Today\'s date is Saturday, 7/31/2021 and name1 is : {name}'
        print(x)


    def zipfunc(self):
        ages = [19, 21, 58, 29]
        eye_colors = ['brown',  'brown', 'brown', 'brown']
        names = ['Thao', 'HangXom0', 'MinhHue', 'Hangxom2']
        for age, eye_color, name in zip(ages, eye_colors, names):
            if age <20:
                print (f'name2: {name}')

#   def argsfunc(arg1, arg2, arg3):
 #      print(arg1, arg2, arg3)

    def kwargsfunc(name, **data):
        print(data)

s1 = Shortcuts()

s1.zipfunc()
s1.escape_quote_func()
args= [1, 2, 3]
#1.argsfunc(*args)

kwargs= {"arg1": 1, "arg2": 2, "arg3":3 }

#city='Vancouver', state='WA', phone='3609900000'
s1.kwargsfunc(city='Vancouver', state='WA', phone='3609900000')
