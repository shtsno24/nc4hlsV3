ulimit -a && ulimit -c unlimited && ulimit -s unlimited
echo -e "Decoder Test\n"
# g++ -Wall -Wextra -std=gnu++11 -o ./log/DecoderTest.out AddDecoderTest.cpp && echo -e "Without Dump Test : Compile Done\n" && ./log/DecoderTest.out && echo "Without Dump Test : Done"
g++ -Wall -Wextra -std=gnu++11 -DDUMP_LOG_ADD -g3 -o ./log/DecoderTest.out AddDecoderTest.cpp && echo -e "With Dump Test : Compile Done\n" && ./log/DecoderTest.out && echo "With Dump Test : Done"
echo -e "Integration Test\n"
# g++ -Wall -Wextra -std=gnu++11 -g3 -o ./log/IntegrationTest.out AddIntegrationTest.cpp && echo -e "Without Dump Test : Compile Done\n" && ./log/IntegrationTest.out && echo "Without Dump Test : Done"
g++ -Wall -Wextra -std=gnu++11 -DDUMP_LOG_ADD -DDUMP_LOG_DSP -g3 -o ./log/IntegrationTest.out AddIntegrationTest.cpp && echo -e "With Dump Test : Compile Done\n" && ./log/IntegrationTest.out && echo "With Dump Test : Done"
