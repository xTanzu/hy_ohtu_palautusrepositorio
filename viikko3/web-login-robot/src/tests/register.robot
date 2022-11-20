*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset And Go To Register Page
#Test Teardown  Reset Application

*** Variables ***
${USERNAME_FAIL_MESSAGE}  Username must consist of letters a-z and be atleast 3 characters long
${PASSWORD_FAIL_MESSAGE}  Password must consist of letters a-Z digits 0-9, be atleast 8 characters long and contain at least 1 character and 1 digit
${PASSWORD_CONFIRMATION_FAIL_MESSAGE}  Password does not match confirmation

*** Test Cases ***
Register With Valid Username And Password
    Set Registration Info  kalle  kalle123  kalle123
    Submit Registration Info
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Registration Info  ka  kalle123  kalle123
    Submit Registration Info
    Registration Should Fail On Username

Register With Valid Username And Too Short Password
    Set Registration Info  kalle  kalle  kalle
    Submit Registration Info
    Registration Should Fail On Password

Register With Nonmatching Password And Password Confirmation
    Set Registration Info  kalle  kalle123  kalle
    Submit Registration Info
    Registration Should Fail On Password Confirmation

Login After Successful Registration
    Set Registration Info  kalle  kalle123  kalle123
    Submit Registration Info
    Registration Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Login Credentials  kalle  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Registration Info  kalle  kalle  kalle
    Submit Registration Info
    Registration Should Fail On Password
    Go To Login Page
    Login Page Should Be Open
    Set Login Credentials  kalle  kalle
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Registration Info
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Set Registration Username  ${username}
    Set Registration Password  ${password}
    Set Registration Password Confirmation  ${password_confirmation}

Set Registration Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Registration Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Registration Password Confirmation
    [Arguments]  ${password_confimation}
    Input Password  password_confirmation  ${password_confimation}

Submit Registration Info
    Click Button  Register

Registration Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Registration Should Fail On Username
    Page Should Contain  ${USERNAME_FAIL_MESSAGE}

Registration Should Fail On Password
    Page Should Contain  ${PASSWORD_FAIL_MESSAGE}

Registration Should Fail On Password Confirmation
    Page Should Contain  ${PASSWORD_CONFIRMATION_FAIL_MESSAGE}
