from State import *
from Map import *
from US_States import *


categories = ["Very Fat", "Quite Fat", "Medium Fat", "Little Fat", "Just Fat", "Neutral", "Just Thin", "Little Thin",
              "Medium Thin", "Quite Thin", "Very Thin"]

us_states = [alabama, arizona, arkansas, california, colorado, connecticut, delaware, florida, georgia, idaho,
          illinois, indiana, iowa, kansas, kentucky, louisiana, maine, maryland, massachusetts, michigan, minnesota,
          mississippi, missouri, montana, nebraska, nevada, new_hampshire, new_jersey, new_mexico, new_york,
          north_carolina, north_dakota, ohio, oklahoma, oregon, pennsylvania, rhode_island, south_carolina,
          south_dakota, tennessee, texas, utah, vermont, virginia, west_virginia, washington, wisconsin, wyoming]
us = Map(us_states)


def reset_states():
    us.convert_state(alabama, "Just Fat")
    us.convert_state(arizona, "Just Thin")
    us.convert_state(arkansas, "Neutral")
    us.convert_state(california, "Little Thin")
    us.convert_state(colorado, "Very Thin")
    us.convert_state(connecticut, "Just Thin")
    us.convert_state(delaware, "Quite Fat")
    us.convert_state(florida, "Just Fat")
    us.convert_state(georgia, "Just Thin")
    us.convert_state(idaho, "Little Thin")
    us.convert_state(illinois, "Little Fat")
    us.convert_state(indiana, "Medium Fat")
    us.convert_state(iowa, "Little Fat")
    us.convert_state(kansas, "Neutral")
    us.convert_state(kentucky, "Little Fat")
    us.convert_state(louisiana, "Little Fat")
    us.convert_state(maine, "Just Thin")
    us.convert_state(maryland, "Just Thin")
    us.convert_state(massachusetts, "Just Thin")
    us.convert_state(michigan, "Medium Fat")
    us.convert_state(minnesota, "Just Thin")
    us.convert_state(mississippi, "Quite Fat")
    us.convert_state(missouri, "Just Fat")
    us.convert_state(montana, "Medium Thin")
    us.convert_state(nebraska, "Just Fat")
    us.convert_state(nevada, "Neutral")
    us.convert_state(new_hampshire, "Little Thin")
    us.convert_state(new_jersey, "Neutral")
    us.convert_state(new_mexico, "Medium Thin")
    us.convert_state(new_york, "Little Thin")
    us.convert_state(north_carolina, "Little Fat")
    us.convert_state(north_dakota, "Just Fat")
    us.convert_state(ohio, "Just Fat")
    us.convert_state(oklahoma, "Just Thin")
    us.convert_state(oregon, "Just Fat")
    us.convert_state(pennsylvania, "Medium Fat")
    us.convert_state(rhode_island, "Just Thin")
    us.convert_state(south_carolina, "Little Fat")
    us.convert_state(south_dakota, "Just Thin")
    us.convert_state(tennessee, "Just Fat")
    us.convert_state(texas, "Just Thin")
    us.convert_state(utah, "Medium Thin")
    us.convert_state(vermont, "Just Thin")
    us.convert_state(virginia, "Just Fat")
    us.convert_state(washington, "Just Thin")
    us.convert_state(west_virginia, "Medium Fat")
    us.convert_state(wisconsin, "Just Fat")
    us.convert_state(wyoming, "Neutral")


def simulate_forward(n):
    for i in range(n):
        us.forward_one_year()


def main(n):
    results = {}
    for state in us_states:
        results[state.get_name()] = {category: 0 for category in categories}

    for i in range(n):
        simulate_forward(25)
        categories_dict = us.list_categories()
        for state in us.states:
            results[state.get_name()][categories_dict[state.get_name()]] += 1
        reset_states()
    return results


if __name__ == '__main__':
    print(main(1000))
