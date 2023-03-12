# python3
# Kristaps Arnolds Kaidalovs 16.grupa 201RDK001

def parallel_processing(n, m, data):
    threads = [0] * n
    output = []

    for job in data:
        # find the next available thread
        next = 0
        for i in range(0, n):
            if threads[next] > threads[i]:
                next = i
        
        # note down the next thread used and start time of it's usage
        output.append((next, threads[next]))
        # increment the total time spent on the next thread
        threads[next] = threads[next] + job

    return output

def main():
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # checks if job count matches the input specified
    if len(data) != m:
        raise RuntimeError(f"Mismatching job count (got {len(data)}, expected {m})")

    # calculate the processing order and start times
    result = parallel_processing(n,m,data)

    # print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
