*** Settings ***
Resource  resource.robot
Test Setup  Input Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jussi  jussi123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  jussi  jussi123
    Output Should Contain  New user registered
    Input Create User
    Input Credentials  jussi  jussi123
    Output Should Contain  User with username jussi already exists

Register With Too Short Username And Valid Password
    Input Credentials   ju  jussi123
    Output Should Contain  Username has to be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  jussi  ju
    Output Should Contain  Password has to be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jussi  jussijussi
    Output Should Contain  Password cannot contain only letters
