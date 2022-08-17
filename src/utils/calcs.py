


def calculate_pass_rating(pass_att: int, pass_yds: int, pass_tds: int, completions: int, ints: int) -> float:

	if pass_att == 0:
		return 0
	else:
		pass_rating = ((8.4 * pass_yds) + (330 * pass_tds) + (100 * completions) - (200 * ints)) / pass_att
		return round(pass_rating, 1)
