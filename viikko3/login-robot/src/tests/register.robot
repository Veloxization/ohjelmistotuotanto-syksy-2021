*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  tester  tests123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  existential  cr151535
    Output Should Contain  User with username existential already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  v4lidp4ssword
    Output Should Contain  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  validuser  short
    Output Should Contain  Password must be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  validuser  longpassword
    Output Should Contain  Password must contain more than just letters

*** Keywords ***
Input New Command And Create User
    Create User  existential  crisises123
    Input New Command