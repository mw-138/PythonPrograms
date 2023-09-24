import helpers


class Team:
    def __init__(self, label):
        self.label = label
        self.games_won = 0
        self.games_drawn = 0
        self.games_lost = 0
        self.goals_for = 0
        self.goals_against = 0

    def get_games_played(self):
        return self.games_lost + self.games_drawn + self.games_won

    def get_goal_difference(self):
        return self.goals_for - self.goals_against

    def get_points(self):
        return (self.games_won * 3) + self.games_drawn


class Fixture:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team


class League:
    def __init__(self, label, teams):
        self.label = label
        self.teams = teams
        self.fixtures = self.__calculate_fixtures()

    def __calculate_fixtures(self):
        fixtures = []
        return fixtures

    def __simulate_fixtures(self):
        pass

    def sort_league(self):
        self.teams.sort(key=lambda x: x.get_points(), reverse=True)

    def print_league(self):
        to_print = []
        pos = 1
        for team in self.teams:
            to_print.append(
                f"{pos} | {team.label} | {team.get_games_played()} | {team.games_won} | {team.games_drawn} | {team.games_lost} | {team.goals_for} | {team.goals_against} | {team.get_goal_difference()} | {team.get_points()}")
            pos += 1
        helpers.print_string_section('-', to_print)


class FootballLeagueTable:
    def __init__(self):
        self.league = League("Premier League", [
            Team("Arsenal FC"),
            Team("Aston Villa"),
            Team("Bournemouth"),
            Team("Brentford"),
            Team("Brighton"),
            Team("Burnley"),
            Team("Chelsea"),
            Team("Crystal Palace"),
            Team("Everton"),
            Team("Fulham"),
            Team("Liverpool"),
            Team("Luton Town"),
            Team("Manchester City"),
            Team("Manchester United"),
            Team("Newcastle United"),
            Team("Nottingham Forest"),
            Team("Sheffield United"),
            Team("Tottenham Hotspur"),
            Team("West Ham"),
            Team("Wolverhampton Wanderers"),
        ])

    def start(self):
        self.league.sort_league()
        self.league.print_league()
