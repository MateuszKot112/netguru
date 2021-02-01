# Automation tests for netguru

This is bdd approach with python and behave aframework.

Preconditions:
You have installed python and pip on your machine

Steps to run tests:
1. In terminal/cmd type cd path\to\directory\netguru_env\Scripts (on linux/macOS  cd path/to/directory/netguru_env/bin)
2. Type in: activate 
3. Return to main folder (or type something like ../..)
4. To run tests type: behave
5. You can run certan tests with command behavve --tags={name of the tag}
6. Available tags are: register, login, valid, invalid
