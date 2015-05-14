class Force:
    alignment = "Light"

    def __init__(self):
        pass

    def use(self):
        print("Using the Force...")

Luke = Force()
print(Luke.alignment)
Luke.use()
