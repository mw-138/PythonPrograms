import helpers


class TicTacToe:
    def __init__(self):
        self.is_player_turn = True
        self.is_game_active = True
        self.player_symbol = "x"
        self.ai_symbol = "o"
        self.empty_symbol = "-"
        self.grid = [self.empty_symbol] * 9

        while self.is_game_active:
            self.__ask_for_input()

    def __print_grid(self):
        print(f"{self.grid[0]} | {self.grid[1]} | {self.grid[2]}\n"
              f"{self.grid[3]} | {self.grid[4]} | {self.grid[5]}\n"
              f"{self.grid[6]} | {self.grid[7]} | {self.grid[8]}")

    def __change_slot_char(self, index, char):
        if not helpers.is_list_index_valid(self.grid, index):
            return
        self.grid[index] = char

    def __get_random_grid_index(self):
        return self.grid.index(self.empty_symbol)

    def __ask_for_input(self):
        self.__print_grid()
        grid_char = self.player_symbol if self.is_player_turn else self.ai_symbol
        try:
            index = int(input("Enter position: "))
            self.__change_slot_char(index, grid_char)
        except ValueError:
            print("Invalid input")

        has_winner, winner_symbol = self.__check_for_winner()
        print(has_winner, winner_symbol)

        if has_winner:
            did_player_win = winner_symbol == self.player_symbol
            did_ai_win = winner_symbol == self.ai_symbol
            self.__winner_found(did_player_win, did_ai_win)
            self.__print_grid()
        else:
            self.is_player_turn = not self.is_player_turn

    def __draw_game(self):
        self.is_game_active = False
        print("Game drawn!")

    def __winner_found(self, player_win, ai_win):
        self.is_game_active = False
        if player_win:
            print("Player won!")
        elif ai_win:
            print("AI won!")

    def __get_remaining_empty_slots(self):
        empty_slots = 0
        for slot in self.grid:
            if slot == "-":
                empty_slots += 1
        return empty_slots

    # TODO: Fix combinations not returning correct bool value
    def __check_for_winner(self):
        conditions = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
            [0, 3, 6],  # Left column
            [1, 4, 7],  # Middle column
            [2, 5, 8],  # Right column
            [0, 4, 8],  # Diagonal from top-left to bottom-right
            [2, 4, 6]  # Diagonal from top-right to bottom-left
        ]

        for condition in conditions:
            # condition_length = len(condition)
            # current_condition_length = 0
            # for index in condition:
            #     if self.grid[index] == self.player_symbol:
            #         current_condition_length += 1
            #         if current_condition_length == condition_length:
            #             return True, self.player_symbol
            #     elif self.grid[index] == self.ai_symbol:
            #         current_condition_length += 1
            #         if current_condition_length == condition_length:
            #             return True, self.ai_symbol
            for index in condition:
                if all(self.grid[index] == self.player_symbol for position in condition):
                    return True, self.player_symbol
                elif all(self.grid[index] == self.ai_symbol for position in condition):
                    return True, self.ai_symbol

        return False, None
