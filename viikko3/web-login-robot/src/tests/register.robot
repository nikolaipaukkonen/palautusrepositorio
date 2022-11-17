*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  palle
    Set Password  palle123
    Set Password Confirmation  palle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pa
    Set Password  palle123
    Set Password Confirmation  palle123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  palle
    Set Password  p
    Set Password Confirmation  p
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  palle
    Set Password  palle123
    Set Password Confirmation  palle1234
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation must match

Login After Successful Registration
    Set Username  palle
    Set Password  palle123
    Set Password Confirmation  palle123
    Submit Credentials
    Go To Login Page
    Set Username  palle
    Set Password  palle123
    Click Button  Login
    Main Page Should Be Open


Login After Failed Registration
    Set Username  palle
    Set Password  palle123
    Set Password Confirmation  palle123
    Submit Credentials
    Go To Login Page
    Set Username  palle
    Set Password  palle321
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
