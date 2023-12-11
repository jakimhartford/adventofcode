#include <iostream>
#include <vector>

long long calculateWaysToBeatRecord(std::vector<int> times, std::vector<int> distances) {
    long long totalWays = 1;

    for (size_t i = 0; i < times.size(); ++i) {
        int time = times[i];
        int distance = distances[i];
        int waysToWin = 0;

        for (int holdTime = 0; holdTime < time; ++holdTime) {
            int totalDistance = 0;
            int remainingTime = time - holdTime;

            for (int t = 0; t < remainingTime; ++t) {
                totalDistance += holdTime;
            }

            if (totalDistance > distance) {
                waysToWin += 1;
            }
        }

        totalWays *= waysToWin;
    }

    return totalWays;
}

int main() {
    std::vector<int> times = {59707878};
    std::vector<int> distances = {430121812131276};
    long long result = calculateWaysToBeatRecord(times, distances);
    std::cout << "Total number of ways to win all races: " << result << std::endl;

    return 0;
}
