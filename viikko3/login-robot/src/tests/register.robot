*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Create User  tester  tests123

Register With Already Taken Username And Valid Password
    Create User  existential  cr1sises
    Output Should Contain  User with username existential already exists

Register With Too Short Username And Valid Password
    Create User  a  v4lidp4ssword
    Output Should Contain  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Create User  valid  2short
    Output Should Contain  Password must be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  valid longpasswordwithonlyletters
    Output Should Contain  Password must not be only letters

*** Keywords ***
Input New Command And Create User
    Create User  existential  crisises123
    Input  New Command