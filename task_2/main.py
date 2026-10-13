from guess_game import make_secret, play


def main():
    secret = make_secret()
    play(secret)


if __name__ == "__main__":
    main()