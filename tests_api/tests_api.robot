*** Settings ***
Library     RequestsLibrary
Library     Collections


*** Variables ***
${Base_URL}             https://mock-api-h0g7.onrender.com/
${API_KEY}              Cle-API-ReqRes-test-academy
${FirstName_Attendu}    Brahim3
${LastName_Attendu}     Nid Moussa
${Email_Attendu}        brahim.nidmoussa@api.testacademy.fr


*** Test Cases ***
Test Requete POST
    &{headers}=    Create Dictionary    Authorization=Bearer ${API_KEY}
    &{Corps_Requete}=    Create Dictionary
    ...    first_name=${FirstName_Attendu}
    ...    last_name=${LastName_Attendu}
    ...    email=${Email_Attendu}
    ${Reponse}=    POST    ${Base_URL}api/users    json=${Corps_Requete}    headers=${headers}    expected_status=201
    Log    ${Reponse.json()}
    Dictionary Should Contain Key    ${Reponse.json()}    id
    Dictionary Should Contain Key    ${Reponse.json()}    createdAt
    ${first_name}=    Get From Dictionary    ${Reponse.json()}    first_name
    Should Be Equal As Strings    ${FirstName_Attendu}    ${first_name}
    ${last_name}=    Get From Dictionary    ${Reponse.json()}    last_name
    Should Be Equal As Strings    ${LastName_Attendu}    ${last_name}
    ${email}=    Get From Dictionary    ${Reponse.json()}    email
    Should Be Equal As Strings    ${Email_Attendu}    ${email}
