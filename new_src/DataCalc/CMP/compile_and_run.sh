ulimit -a && ulimit -c unlimited && ulimit -s unlimited
echo -e "Layer Test\n"
# g++ -Wall -Wextra -std=gnu++11 -o ./log/LayerTest.out CMPTest.cpp && echo -e "Without Dump Test : Compile Done\n" && ./log/LayerTest.out && echo "Without Dump Test : Done"
g++ -Wall -Wextra -std=gnu++11 -DDUMP_LOG_CMP -g3 -o ./log/LayerTest.out CMPTest.cpp && echo -e "With Dump Test : Compile Done\n" && ./log/LayerTest.out && echo "With Dump Test : Done"
