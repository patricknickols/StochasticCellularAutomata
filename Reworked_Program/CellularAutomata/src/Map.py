class Map:

    def __init__(self, state_list):
        self.states = state_list

    def forward_one_year(self):
        new_states = {}
        for state in self.states:
            new_states[state] = state.forward_year()
        for entry in new_states:
            self.convert_state(entry, new_states[entry])

    def list_categories(self):
        return {state.get_name(): state.return_category() for state in self.states}

    def convert_state(self, state, new_category):
        new_state = state.transition_to(new_category)
        for sta in self.states:
            if state.name == sta.name:
                self.states.remove(sta)
        self.states.append(new_state)

    def categorise_states(self):
        for state in self.states:
            state.categorise_state()

    def get_category(self, state_name):
        for state in self.states:
            if state.name == state_name:
                return state.return_category()



