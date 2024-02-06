if __name__ == '__main__':
    name_score = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score[name] = score

    scores = list(name_score.values())
    names = list(name_score.keys())
    sort_score = sorted(set(scores))
    second_lowest_score = sort_score[1]
    sorted_names_by_lowest_score = sorted([name for name, score in zip(names, scores)
                                           if score == second_lowest_score])
    print("\n".join(sorted_names_by_lowest_score))

