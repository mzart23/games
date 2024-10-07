from clases import Fighter,Monster,Sword,Bow


# Пример использования
def main():
    fighter = Fighter("Боец")
    monster = Monster()

    # Выбор меча
    sword = Sword()
    fighter.change_weapon(sword)
    fighter.attack(monster)

    # Выбор лука
    bow = Bow()
    fighter.change_weapon(bow)
    fighter.attack(monster)

if __name__ == "__main__":
    main()