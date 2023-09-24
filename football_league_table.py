import random

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

    def sort_condition(self):
        return self.get_points(), self.get_goal_difference()


class Fixture:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

    def determine_winner(self):
        home_score = helpers.random_inclusive(0, 3)
        away_score = helpers.random_inclusive(0, 3)

        self.home_team.goals_for += home_score
        self.away_team.goals_for += away_score
        self.home_team.goals_against += away_score
        self.away_team.goals_against += home_score

        if home_score == away_score:
            self.home_team.games_drawn += 1
            self.away_team.games_drawn += 1
        elif home_score > away_score:
            self.home_team.games_won += 1
            self.away_team.games_lost += 1
        elif home_score < away_score:
            self.home_team.games_lost += 1
            self.away_team.games_won += 1


class League:
    def __init__(self, label, teams, team_dividers):
        self.label = label
        self.teams = teams
        self.fixtures = self.__generate_fixtures()
        self.team_dividers = team_dividers

    def __generate_fixtures(self):
        fixtures = []

        for team_a in self.teams:
            for team_b in self.teams:
                if team_a != team_b:
                    fixtures.append(Fixture(team_a, team_b))

        random.shuffle(fixtures)
        return fixtures

    def get_fixtures_for_team(self, team):
        fixtures = []

        for fixture in self.fixtures:
            if team == fixture.home_team or team == fixture.away_team:
                fixtures.append(fixture)

        return fixtures

    def simulate_fixtures(self):
        for fixture in self.fixtures:
            fixture.determine_winner()

    def sort_league(self):
        self.teams.sort(key=lambda x: x.sort_condition(), reverse=True)

    def print_league(self):
        to_print = [f"{self.label}\n"]
        pos = 1

        for team in self.teams:
            to_print.append(
                f"{pos} | "
                f"{team.label} | "
                f"GP: {team.get_games_played()} | "
                f"W: {team.games_won} | "
                f"D: {team.games_drawn} | "
                f"L: {team.games_lost} | "
                f"GF: {team.goals_for} | "
                f"GA: {team.goals_against} | "
                f"GD: {team.get_goal_difference()} | "
                f"PTS: {team.get_points()}"
            )
            pos += 1

        for divider in self.team_dividers:
            to_print.insert(divider + 1, "-" * helpers.get_list_max_length(to_print))

        helpers.print_string_section('-', to_print)


class FootballLeagueTable:
    def __init__(self):
        self.league = premier_league

    def start(self):
        self.league.simulate_fixtures()
        self.league.sort_league()
        self.league.print_league()


premier_league = League("Premier League", [
    Team("Arsenal"),
    Team("Aston Villa"),
    Team("Bournemouth"),
    Team("Brentford"),
    Team("Brighton And Hover Albion"),
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
    Team("West Ham United"),
    Team("Wolverhampton Wanderers")
], [1, 5, 7, 20])
