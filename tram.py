if __name__ == "__main__":
    tram_capacity = 0
    results = []
    n = int(input())

    for _ in range(n):
        passenger_exit, passenger_on_boarding = map(int, input().split())
        tram_capacity += (passenger_on_boarding - passenger_exit)
        results.append(tram_capacity)
    print(max(results))
