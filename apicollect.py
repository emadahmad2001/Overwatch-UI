import requests

"""
Required installments: requests
"""
# API address we can fill the parameters: platform, region and battle tag of a player to get their profile
url = 'https://ow-api.com/v1/stats/{}/{}/{}/complete'


class Overwatch:
    """
    This is the class for the game which keeps track of all the players in it.
    It sends requests to the Overwatch API online to fetch stats of players in the game.
    To fetch the results the user needs to input a valid platform, region and battle tag of their account.
    """

    def __init__(self, platform, region, battle_tag):
        self.information = [platform, region, battle_tag]
        # Send a request to the api to get information about the user profile
        self.result = requests.get(url.format(platform, region, battle_tag))
        # Convert to JSON (basically dictionary formatted info)
        self.result_json = self.result.json()
        # List of all filters for player to select
        self.displayed_filters = []
        self.api_filters = []
        self.sub_stats = []

    def get_filters(self):
        """
        Get the main filters(stats) available for a user to select to compare with another player.
        We don't really care about icon, level icon, etc. for this since they aren't stats used for comparision.

        :return: list of possible filters
        """

        # The primary filters
        self.displayed_filters = ['Name', 'Level', 'Prestige', 'Rating', 'Endorsement Level', 'In-Game Stats',
                                  'Best In-Game Stats', 'Game Outcomes', 'Awards']
        self.api_filters.extend(
            ['name', 'level', 'prestige', 'rating', 'Endorsement Level', 'In-Game Stats', 'Best In-Game Stats',
             'Game Outcomes', 'Awards'])

        filter_dict = {}

        for x, stat in enumerate(self.displayed_filters):
            filter_dict[stat] = self.api_filters[x]

        return filter_dict

    def get_stat(self, find_filter, game_mode):
        """
        Retrieve the required stat from the api, based on the user choice and game mode.
        Certain stats/filters are not applicable for all gamers and as such they are not
        listed in the API. N/A is used for such cases.

        :return: A stat from the api based on inputted game mode and filter
        """
        try:
            if find_filter == 'Name':
                return self.result_json['name']
            elif find_filter == 'Level':
                return self.result_json['level']
            elif find_filter == 'Endorsement Level':
                return self.result_json['endorsement']
            elif find_filter == 'Rating':
                return self.result_json['rating']
            elif find_filter == 'Prestige':
                return self.result_json['prestige']
            elif find_filter in ['cards', 'medals', 'medalsBronze', 'medalsSilver', 'medalsGold']:
                return self.result_json[game_mode]['awards'][find_filter]
            elif find_filter in ['gameWon', 'gamesLost', 'gamesPlayed']:
                return self.result_json[game_mode]['careerStats']['allHeroes']['game'][find_filter]
            elif find_filter in ['allDamageDoneMostInGame', 'barrierDamageDoneMostInGame', 'eliminationsMostInGame',
                                 'healingDoneMostInGame', 'killsStreakBest', 'multikillsBest']:
                return self.result_json[game_mode]['careerStats']['allHeroes']['best'][find_filter]
            elif find_filter in ['barrierDamageDone', 'damageDone', 'deaths', 'eliminations', 'soloKills',
                                 'objectiveKills']:
                return self.result_json[game_mode]['careerStats']['allHeroes']['combat'][find_filter]
            else:
                return self.result_json[find_filter]
        except TypeError:
            # If the api does not have the information associated with a profile
            return 'N/A'
        except KeyError:
            return 'N/A'
