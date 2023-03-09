def get_result(final_score):
    if final_score["home_score"] > final_score["away_score"]:
        return "Home Win"
    
    if final_score["away_score"] > final_score["home_score"]:
        return "Away win"
    
    return "Draw"

