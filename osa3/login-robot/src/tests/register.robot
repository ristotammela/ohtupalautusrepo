*** Settings ***
Resource  resource.robot


*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  mikko  mikko123
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Create User  mikko  mikko123
    Input New Command
    Input Credentials  mikko  mikko321
    Output Should Contain  User with username mikko already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  mi  mikko123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  mikko123  mikko123
    Output Should Contain  Username must contain only letters a-z

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  mikko  mikko1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  mikko  mikkoabc
    Output Should Contain  Password must not consist only of letters


*** Keywords ***
