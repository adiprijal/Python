# def hello(**kwargs):
def hello(**self):
    print("Hello,",self['first'] +' '+ self['last']+'.')

hello(first='Adip',middle='jung',last='Rijal')