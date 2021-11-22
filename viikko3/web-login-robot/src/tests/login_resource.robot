*** Settings ***
Library  ../AppLibrary.py
Resource  resource.robot

*** Keywords ***
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
    Click Button  Login

Submit Registration
    Click Button  Register

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Page Should Be Open
    Title Should Be  Register

Input Registration Credentials
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password}