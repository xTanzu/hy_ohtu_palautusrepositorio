*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Register With Credentials  pikkukalle  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  pikkukalle  salasana123
    Register With Credentials  pikkukalle  salasana456
    Output Should Contain  User with username pikkukalle already exists

Register With Too Short Username And Valid Password 
    Register With Credentials  pk  salasana123
    Output Should Contain  Username must consist of letters a-z and be atleast 3 characters long

Register With Valid Username And Too Short Password
    Register With Credentials  pikkukalle  salsana
    Output Should Contain  Password must consist of letters a-Z digits 0-9, be atleast 8 characters long and contain at least 1 character and 1 digit

Register With Valid Username And Long Enough Password Containing Only Letters
    Register With Credentials  pikkukalle  salasana
    Output Should Contain  Password must consist of letters a-Z digits 0-9, be atleast 8 characters long and contain at least 1 character and 1 digit
    
