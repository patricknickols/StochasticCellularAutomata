import numpy as np
import unittest
import US_States
import Map
import State
import helper_functions


class TestCA(unittest.TestCase):

    def test_states_can_transition(self):
        # ARRANGE
        fake_state = State.VeryFatState("Fake", [])
        new_map = Map.Map([fake_state])

        # ACT
        new_map.convert_state(fake_state, "Very Thin")

        # ASSERT
        self.assertEqual(new_map.list_categories()["Fake"], "Very Thin")

    def test_generic_border_influence_works_as_intended(self):
        # ARRANGE
        matrix = np.zeros((11, 11))
        test_state = State.VeryFatState("Test", [])
        fake_state = State.VeryFatState("Fake", [])

        # ACT
        test_state.trans_matrix = matrix
        fake_state.influence_border_state(test_state)

        # ASSERT
        self.assertTrue(test_state.trans_matrix[10, 0] > 0)

    def test_state_border_probabilities_affect_correctly(self):
        # ARRANGE
        fake_state = State.VeryFatState("Fake", [])
        thin_state = State.VeryThinState("Thin", [])
        fake_state.add_border_states([thin_state])

        # ACT
        prob_fake_to_very_thin = fake_state.trans_matrix[0, 10]
        thin_state.influence_border_state(fake_state)
        prob2_fake_to_very_thin = fake_state.trans_matrix[0, 10]

        # ASSERT
        self.assertTrue(prob2_fake_to_very_thin > prob_fake_to_very_thin)

    def test_transitions_can_be_induced(self):
        # ARRANGE
        test_state1 = State.VeryThinState("1", [])
        test_state2 = State.VeryFatState("2", [])
        test_state3 = State.VeryFatState("3", [])
        test_state1.add_border_states([test_state2, test_state3])
        test_state2.add_border_states([test_state1, test_state3])
        test_state3.add_border_states([test_state1, test_state2])
        test_map = Map.Map([test_state1, test_state2, test_state3])

        # ACT
        test_map.forward_one_year()

        # ASSERT
        self.assertTrue(test_map.get_category("1") != "Very Thin")

    def test_increase_matrix_diagonals_works_as_intended(self):
        # ARRANGE
        test_matrix = np.zeros((11, 11))
        test_matrix[0, 10] = 1000

        # ACT
        State.increase_matrix_diagonals(test_matrix, 0, 1)

        # ASSERT
        self.assertEqual(test_matrix[5, 5], 1)

    def test_increase_matrix_diagonals_works_in_right_direction(self):
        # ARRANGE
        test_matrix = np.zeros((11, 11))
        test_matrix[0, 10] = 1000

        # ACT
        State.increase_matrix_diagonals(test_matrix, 1, 1)

        # ASSERT
        self.assertEqual(test_matrix[5, 6], 1)

    def test_row_sums_are_unchanged_by_very_fat_influence(self):
        # ARRANGE
        test_state1 = State.VeryThinState("1", [])
        test_state2 = State.VeryFatState("2", [])
        before_matrix = test_state1.trans_matrix.copy()

        # ACT
        test_state2.influence_border_state(test_state1)
        after_matrix = test_state1.trans_matrix

        # ASSERT
        self.assertTrue(before_matrix[0, 0] != after_matrix[0, 0])
        self.assertAlmostEqual(np.sum(before_matrix[4]), np.sum(after_matrix[4]))




