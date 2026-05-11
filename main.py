from partie import init_joueurs, jouer_partie

def main():
    joueurs = init_joueurs()

    jouer_partie(joueurs)

if __name__ == "__main__":
    main()