ulimit -a && ulimit -c unlimited && ulimit -s unlimited
echo -e "Memory Unit Test\n"
# g++ -Wall -Wextra -std=gnu++11 -o ./log/MemoryUnitTest.out MemoryUnitTest.cpp && echo -e "Without Dump Test : Compile Done\n" && ./log/MemoryUnitTest.out && echo "Without Dump Test : Done"
g++ -Wall -Wextra -std=gnu++11 -DDUMP_LOG_DATA_BANK_A -DDUMP_LOG_DATA_BANK_B -DDUMP_LOG_WEIGHT_BANK -g3 -o ./log/MemoryUnitTest.out MemoryUnitTest.cpp && echo -e "With Dump Test : Compile Done\n" && ./log/MemoryUnitTest.out && echo "With Dump Test : Done"
