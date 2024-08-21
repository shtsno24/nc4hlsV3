ulimit -a && ulimit -c unlimited && ulimit -s unlimited
echo -e "Layer Test\n"
# g++ -Wall -Wextra -std=gnu++11 -o ./log/DSPTest.out DSPTest.cpp && echo -e "Without Dump Test : Compile Done\n" && ./log/DSPTest.out && echo "Without Dump Test : Done"
g++ -Wall -Wextra -std=gnu++11 -DDUMP_LOG_DSP -g3 -o ./log/DSPTest.out DSPTest.cpp && echo -e "With Dump Test : Compile Done\n" && ./log/DSPTest.out && echo "With Dump Test : Done"
