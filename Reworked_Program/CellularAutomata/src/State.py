import random
from abc import ABC
from re import match

import numpy as np

col_to_cat = {0: "Very Fat", 1: "Quite Fat", 2: "Medium Fat", 3: "Little Fat", 4: "Just Fat", 5: "Neutral",
              6: "Just Thin", 7: "Little Thin", 8: "Medium Thin", 9: "Quite Thin", 10: "Very Thin"}
cat_to_row = {"Very Fat": 0, "Quite Fat": 1, "Medium Fat": 2, "Little Fat": 3, "Just Fat": 4, "Neutral": 5,
              "Just Thin": 6, "Little Thin": 7, "Medium Thin": 8, "Quite Thin": 9, "Very Thin": 10}


def increase_matrix_diagonals(matrix, diagonal_offset, increment):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if j == i + diagonal_offset:
                proposed_result = matrix[i, j] + increment
                if proposed_result > 1000:
                    matrix[i, j] = 999
                elif proposed_result < 0:
                    matrix[i, j] = 1
                else:
                    matrix[i, j] = proposed_result


def generic_influence_border_state(influenced_state, d):
    increase_matrix_diagonals(influenced_state.trans_matrix, -1, d)
    increase_matrix_diagonals(influenced_state.trans_matrix, -2, d / 2)
    increase_matrix_diagonals(influenced_state.trans_matrix, -3, d / 4)
    increase_matrix_diagonals(influenced_state.trans_matrix, -4, d / 8)
    increase_matrix_diagonals(influenced_state.trans_matrix, -5, d / 16)
    increase_matrix_diagonals(influenced_state.trans_matrix, -6, d / 32)
    increase_matrix_diagonals(influenced_state.trans_matrix, -7, d / 64)
    increase_matrix_diagonals(influenced_state.trans_matrix, -8, d / 128)
    increase_matrix_diagonals(influenced_state.trans_matrix, -9, d / 256)
    increase_matrix_diagonals(influenced_state.trans_matrix, -10, d / 512)
    increase_matrix_diagonals(influenced_state.trans_matrix, 1, -d / 2)
    increase_matrix_diagonals(influenced_state.trans_matrix, 2, -d / 4)
    increase_matrix_diagonals(influenced_state.trans_matrix, 3, -d / 8)
    increase_matrix_diagonals(influenced_state.trans_matrix, 4, -d / 16)
    increase_matrix_diagonals(influenced_state.trans_matrix, 5, -d / 32)
    increase_matrix_diagonals(influenced_state.trans_matrix, 6, -d / 64)
    increase_matrix_diagonals(influenced_state.trans_matrix, 7, -d / 128)
    increase_matrix_diagonals(influenced_state.trans_matrix, 8, -d / 256)
    increase_matrix_diagonals(influenced_state.trans_matrix, 9, -d / 512)
    increase_matrix_diagonals(influenced_state.trans_matrix, 10, -d / 1024)
    for i in range(11):
        difference = np.sum(influenced_state.trans_matrix[i]) - 1000
        influenced_state.trans_matrix[i, i] -= difference


class State(ABC):

    category = None

    n1 = 256000/1023
    n2 = 128000/767
    n3 = 64000/447
    n4 = 32000/239
    n5 = 16000/123
    n6 = 4000/31
    n7 = n5
    n8 = n4
    n9 = n3
    n10 = n2
    n11 = n1

    trans_matrix = np.matrix([[500    ,      n1,    n1/2,   n1/4,   n1/8,  n1/16, n1/32, n1/64, n1/128, n1/256, n1/512],
                              [n2     ,     500,      n2,   n2/2,   n2/4,   n2/8, n2/16, n2/32,  n2/64, n2/128, n2/256],
                              [n3/2   ,      n3,     500,     n3,   n3/2,   n3/4,  n3/8, n3/16,  n3/32,  n3/64, n3/128],
                              [n4/4   ,    n4/2,      n4,    500,     n4,   n4/2,  n4/4,  n4/8,  n4/16,  n4/32,  n4/64],
                              [n5/8   ,    n5/4,    n5/2,     n5,    500,     n5,  n5/2,  n5/4,   n5/8,  n5/16,  n5/32],
                              [n6/16  ,    n6/8,    n6/4,   n6/2,     n6,    500,    n6,  n6/2,   n6/4,   n6/8,  n6/16],
                              [n7/32  ,   n7/16,    n7/8,   n7/4,   n7/2,     n7,   500,    n7,   n7/2,   n7/4,   n7/8],
                              [n8/64  ,   n8/32,   n8/16,   n8/8,   n8/4,   n8/2,    n8,   500,     n8,   n8/2,   n8/4],
                              [n9/128 ,   n9/64,   n9/32,  n9/16,   n9/8,   n9/4,  n9/2,    n9,    500,     n9,   n9/2],
                              [n10/256, n10/128,  n10/64, n10/32, n10/16,  n10/8, n10/4, n10/2,    n10,    500,    n10],
                              [n11/512, n11/256, n11/128, n11/64, n11/32, n11/16, n11/8, n11/4,  n11/2,    n11,    500]
                              ])

    def __init__(self, name, border_states):
        self.name = name
        self.bordering_states = border_states

    def get_name(self):
        return self.name

    def add_border_states(self, states):
        for state in states:
            self.bordering_states.append(state)

    def forward_year(self):
        for state in self.bordering_states:
            state.influence_border_state(self)
        x = random.random() * 1000
        category = self.return_category()
        row = cat_to_row[category]
        prob_cutoffs = np.cumsum(self.trans_matrix[row])
        for i in range(np.shape(prob_cutoffs)[1]):
            if x <= prob_cutoffs[0, i]:
                new_state_category = col_to_cat[i]
                return new_state_category
        print(f"No valid range. Random number was {x} and largest probability value was {prob_cutoffs[0, 10]}")

    def influence_border_state(self, influenced_state):
        pass

    def transition_to(self, category):
        if category == "Very Fat":
            return VeryFatState(self.name, self.bordering_states)
        elif category == "Quite Fat":
            return QuiteFatState(self.name, self.bordering_states)
        elif category == "Medium Fat":
            return MediumFatState(self.name, self.bordering_states)
        elif category == "Little Fat":
            return LittleFatState(self.name, self.bordering_states)
        elif category == "Just Fat":
            return JustFatState(self.name, self.bordering_states)
        elif category == "Neutral":
            return NeutralState(self.name, self.bordering_states)
        elif category == "Just Thin":
            return JustThinState(self.name, self.bordering_states)
        elif category == "Little Thin":
            return LittleThinState(self.name, self.bordering_states)
        elif category == "Medium Thin":
            return MediumThinState(self.name, self.bordering_states)
        elif category == "Quite Thin":
            return QuiteThinState(self.name, self.bordering_states)
        elif category == "Very Thin":
            return VeryThinState(self.name, self.bordering_states)
        else:
            print(f"Error, state had category {category}")

    def return_category(self):
        return self.category


class VeryFatState(State):
    category = "Very Fat"

    def influence_border_state(self, influenced_state):
        generic_influence_border_state(influenced_state, 200)


class QuiteFatState(State):
    category = "Quite Fat"

    def influence_border_state(self, influenced_state):
        generic_influence_border_state(influenced_state, 150)


class MediumFatState(State):
    category = "Medium Fat"

    def influence_border_state(self, influenced_state):
        generic_influence_border_state(influenced_state, 100)


class LittleFatState(State):
    category = "Little Fat"

    def influence_border_state(self, influenced_state):
        generic_influence_border_state(influenced_state, 75)


class JustFatState(State):
    category = "Just Fat"

    def influence_border_state(self, influenced_state):
        generic_influence_border_state(influenced_state, 50)


class NeutralState(State):
    category = "Neutral"


class JustThinState(State):
    category = "Just Thin"

    def influence_border_state(self, influenced_state):
        generic_influence_border_state(influenced_state, -50)


class LittleThinState(State):
    category = "Little Thin"

    def influence_border_state(self, influenced_state):
        generic_influence_border_state(influenced_state, -75)


class MediumThinState(State):
    category = "Medium Thin"

    def influence_border_state(self, influenced_state):
        generic_influence_border_state(influenced_state, -100)


class QuiteThinState(State):
    category = "Quite Thin"

    def influence_border_state(self, influenced_state):
        generic_influence_border_state(influenced_state, -150)


class VeryThinState(State):
    category = "Very Thin"

    def influence_border_state(self, influenced_state):
        generic_influence_border_state(influenced_state, -200)

