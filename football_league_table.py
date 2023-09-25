import random
import helpers


class Team:
    def __init__(self, label, rating):
        self.label = label
        self.rating = rating
        self.max_rating = 10
        self.games_won = 0
        self.games_drawn = 0
        self.games_lost = 0
        self.goals_for = 0
        self.goals_against = 0

    def get_games_played(self):
        return self.games_won + self.games_drawn + self.games_lost

    def get_goal_difference(self):
        return self.goals_for - self.goals_against

    def get_points(self):
        return (self.games_won * 3) + self.games_drawn

    def sort_condition(self):
        return self.get_points(), self.get_goal_difference()

    def get_win_chance(self):
        return round(self.rating / self.max_rating * 100)

    def clamp_rating(self):
        helpers.clamp(self.rating, 0, self.max_rating)


class Fixture:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

    def determine_winner(self):
        winner_population = [self.home_team, self.away_team]
        winner_weights = (self.home_team.rating, self.away_team.rating)
        winner = random.choices(population=winner_population, weights=winner_weights, k=1)[0]
        did_home_win = self.home_team == winner

        goal_weights = {
            0: 80,
            1: 90,
            2: 60,
            3: 50,
            4: 20,
            5: 5,
            6: 0.5,
            7: 0.5,
            8: 0.5,
            9: 0.5,
            10: 0.5
        }

        rating_change_min = 0.01
        rating_change_max = 0.05
        max_goals_population = []
        max_goals_weights = []

        for key in goal_weights:
            max_goals_population.append(key)
            max_goals_weights.append(goal_weights[key])

        max_goals_to_score = random.choices(population=max_goals_population, weights=max_goals_weights, k=1)[0]

        if did_home_win:
            away_score = helpers.random_inclusive(0, max_goals_to_score)
            home_score = away_score + helpers.random_inclusive(0, max_goals_to_score) + 1
            self.home_team.rating += random.uniform(rating_change_min, rating_change_max)
            self.away_team.rating -= random.uniform(rating_change_min, rating_change_max)
            self.home_team.clamp_rating()
            self.away_team.clamp_rating()
        else:
            home_score = helpers.random_inclusive(0, max_goals_to_score)
            away_score = home_score + helpers.random_inclusive(0, max_goals_to_score) + 1
            self.home_team.rating -= random.uniform(rating_change_min, rating_change_max)
            self.away_team.rating += random.uniform(rating_change_min, rating_change_max)
            self.home_team.clamp_rating()
            self.away_team.clamp_rating()

        self.home_team.goals_for += home_score
        self.away_team.goals_for += away_score
        self.home_team.goals_against += away_score
        self.away_team.goals_against += home_score

        if did_home_win:
            self.home_team.games_won += 1
            self.away_team.games_lost += 1
        elif not did_home_win:
            self.home_team.games_lost += 1
            self.away_team.games_won += 1
        else:
            self.home_team.games_drawn += 1
            self.away_team.games_drawn += 1

        print(f"{self.home_team.label} ({home_score}) vs ({away_score}) {self.away_team.label}")


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
                f"{team.label.upper()} | "
                f"GP: {team.get_games_played()} | "
                f"W: {team.games_won} | "
                f"D: {team.games_drawn} | "
                f"L: {team.games_lost} | "
                f"GF: {team.goals_for} | "
                f"GA: {team.goals_against} | "
                f"GD: {team.get_goal_difference()} | "
                f"PTS: {team.get_points()} | "
                f"WIN CHANCE: {team.get_win_chance()}%"
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
    Team("Arsenal", 8),
    Team("Aston Villa", 6),
    Team("Bournemouth", 5),
    Team("Brentford", 5),
    Team("Brighton And Hover Albion", 7),
    Team("Burnley", 3),
    Team("Chelsea", 4),
    Team("Crystal Palace", 4),
    Team("Everton", 3),
    Team("Fulham", 4),
    Team("Liverpool", 7),
    Team("Luton Town", 2),
    Team("Manchester City", 9),
    Team("Manchester United", 7),
    Team("Newcastle United", 7),
    Team("Nottingham Forest", 5),
    Team("Sheffield United", 2),
    Team("Tottenham Hotspur", 7),
    Team("West Ham United", 6),
    Team("Wolverhampton Wanderers", 5)
], [1, 5, 7, 20])
