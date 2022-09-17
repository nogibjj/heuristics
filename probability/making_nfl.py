#!/usr/bin/env python

nfl_data_2014 = {
    "high_school_players": 1086627,
    "drafted": 256,
    "income_after_tax": 252000,
    "years_to_play": 3,
    "three_year_income": 756000,
    "ncca_players": 70147,
    "hs_to_ncca": 0.065,
    "ncca_to_nfl": 0.016,
    "hs_to_nfl": 0.065 * 0.016,
}
expected_value = nfl_data_2014["hs_to_nfl"] * nfl_data_2014["three_year_income"]
# print odds of making it to the NFL are
print(
    "Odds of making it to the NFL are 1 in %s"
    % (nfl_data_2014["high_school_players"] / nfl_data_2014["drafted"])
)

print(f"Expected value of pursing NFL career: ${round(expected_value, 0)}")
# print percentage of high school players that make it to the NFL rounded to 1 decimal places
print(
    f"Percentage of high school players that make it to the NFL: {nfl_data_2014['hs_to_nfl'] * 100:.1f}%"
)
