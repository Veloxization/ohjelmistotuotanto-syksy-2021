import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict
        )

        if player.nationality == "FIN":
            players.append(player)

    players.sort(reverse=True)
    print("Oliot:")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
