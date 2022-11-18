*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown Close Browser
Test Setup  Reset And Go To Register Page
#Test Teardown  Reset Application

*** Variables ***
${USERNAME_FAIL_MESSAGE}  Username must consist of letters a-z and be atleast 3 characters long
${PASSWORD_FAIL_MESSAGE}  Password must consist of letters a-Z digits 0-9, be atleast 8 characters long and contain at least 1 character and 1 digit
${PASSWORD_CONFIRMATION_FAIL_MESSAGE}  Password does not match confirmation

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Info
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Info
    Register Should Fail On Username

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Register Info
    Register Should Fail On Password

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle
    Submit Register Info
    Register Should Fail On Password Confirmation

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confimation}
    Input Password  password_confirmation  ${password_confimation}

Submit Register Info
    Click Button  Register

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail On Username
    Page Should Contain  ${USERNAME_FAIL_MESSAGE}

Register Should Fail On Password
    Page Should Contain  ${PASSWORD_FAIL_MESSAGE}

Register Should Fail On Password Confirmation
    Page Should Contain  ${PASSWORD_CONFIRMATION_FAIL_MESSAGE}
