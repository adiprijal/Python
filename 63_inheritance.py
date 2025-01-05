class game:
    play="indoor"

    @staticmethod
    def name():
        print("Chess")
    
class player(game):
    player="Adip"

    @staticmethod
    def name():
        print("Chess......")

a=game()
b=player()
a.name()
b.name()
print(b.play)
print(b.player)