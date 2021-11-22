*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  username
    Set Password  v4lidpass
    Set Password Confirmation  v4lidpass
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  v4lidpass
    Set Password Confirmation  v4lidpass
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long and consist of letters a-z

Register With Valid Username And Too Short Password
    Set Username  username
    Set Password  sh0rt
    Set Password Confirmation  sh0rt
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters and can't be only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  username
    Set Password  password123
    Set Password Confirmation  password456
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

*** Keywords ***
Reset And Go To Register Page
    Reset Application
    Go To  ${REGISTER URL}

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Page Should Be Open
    Title Should Be  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${username}
    Input Password  password  ${username}

Set Password Confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}

Submit Credentials
    Click Button  Register
