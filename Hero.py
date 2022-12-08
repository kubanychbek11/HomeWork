class SuperHero:
    people = 'people'

    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def realname(self):
         return f'{self.name}'
    def hpx2(self):
        return f'{self.health_points*2}'
    def __str__(self):
        return  f'{self.nickname, self.superpower, self.health_points}'
    def __int__(self):
        return len(self.catchphrase)
Hero=SuperHero('Алишер', 'Клоун','деньги',666,'все хотят от меня шоу')
Hero.realname()
Hero.hpx2()
Hero.__str__()
Hero.__int__()
print(Hero.realname())
print(Hero.hpx2())
print(Hero.__str__())
print(Hero.__int__())