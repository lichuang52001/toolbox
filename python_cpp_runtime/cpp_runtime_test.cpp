#include <iostream>
#include <chrono>

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();

    // Calculate the sum of the first 10 million numbers
    uint64_t total = 0;
    for (int i = 0; i < 10000000; i++) {
        total += i;
    }

    auto end_time = std::chrono::high_resolution_clock::now();

    std::cout << "Total: " << total << std::endl;
    std::cout << "Time: " << std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count() << " microseconds" << std::endl;

    return 0;
}
