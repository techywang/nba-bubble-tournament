HOME_WON_RESULT = 1


def bubbleWinner(games, results):
    # Write your code here.
    topTeam = ""
    scores = {topTeam: 0}

    for idx, game in enumerate(games):
        result = results[idx]
        homeTeam, awayTeam = game

        winner = homeTeam if result == HOME_WON_RESULT else awayTeam

        updateScores(winner, 3, scores)

        if scores[winner] > scores[topTeam]:
            topTeam = winner

    return topTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points
