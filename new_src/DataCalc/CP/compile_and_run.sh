ulimit -a && ulimit -c unlimited && ulimit -s unlimited
echo -e "Layer Test\n"
# g++ -Wall -Wextra -std=gnu++11 -o ./log/CPTest.out CPTest.cpp && echo -e "Without Dump Test : Compile Done\n" && ./log/CPTest.out && echo "Without Dump Test : Done"
g++ -Wall -Wextra -std=gnu++11 -DDUMP_LOG_CP -g3 -o ./log/CPTest.out CPTest.cpp && echo -e "With Dump Test : Compile Done\n" && ./log/CPTest.out && echo "With Dump Test : Done"
