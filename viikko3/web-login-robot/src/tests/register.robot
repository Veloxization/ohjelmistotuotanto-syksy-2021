*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Input Registration Credentials  username  v4lidpass
    Submit Registration
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Input Registration Credentials  a  v4lidpass
    Submit Registration
    Register Should Fail With Message  Username must be at least 3 characters long and consist of letters a-z

Register With Valid Username And Too Short Password
    Input Registration Credentials  username  sh0rt
    Submit Registration
    Register Should Fail With Message  Password must be at least 8 characters and can't be only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  username
    Set Password  password123
    Set Password Confirmation  password456
    Submit Registration
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Input Registration Credentials  username  v4lidpass
    Submit Registration
    Go To Login Page
    Set Username  username
    Set Password  v4lidpass
    Submit Credentials
    Login Should Succeed
    
Login After Failed Registration
    Input Registration Credentials  a  password123
    Submit Registration
    Go To Login Page
    Set Username  a
    Set Password  password123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset And Go To Register Page
    Reset Application
    Go To  ${REGISTER URL}
