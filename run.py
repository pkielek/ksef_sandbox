import subprocess
import requests

HOST = "ksef-test"
AUTH_TOKEN = "312068b7998590c7ebf3fe3f5c1304c02343e8927325f13acb24a104d9a24a56" # included in Dockerfile, retrieved from https://ksef-test.mf.gov.pl/web/login
NIP = "1111111111" # included in Dockerfile


def get_encrypted_token_and_challenge(build_dockerfile = False):
    # build docker image from local Dockerfile for encrypting key - need to only be ran once
    if build_dockerfile:
        subprocess.run(["docker", "build", "-t" "ksef-java", "."])

    # encode key and get authorization challenge
    stdout_output = subprocess.run(["docker","run","-it","--rm","ksef-java"],capture_output=True).stdout.decode()

    for part in stdout_output.split('\r\n'):
        if 'token: ' in part:
            encrypted_token = [x for x in part.split('token: ') if x][0]
        if 'challenge: ' in part:
            challenge = [x for x in part.split('challenge: ') if x][0]

    return encrypted_token, challenge


def init_token(encrypted_token,challenge,host=HOST,nip=NIP):
    url = f'https://{host}.mf.gov.pl/api/online/Session/InitToken'
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/octet-stream"
    }
    body = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <ns3:InitSessionTokenRequest xmlns="http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001" xmlns:ns2="http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001" xmlns:ns3="http://ksef.mf.gov.pl/schema/gtw/svc/online/auth/request/2021/10/01/0001">
            <ns3:Context>
                <Challenge>{challenge}</Challenge>
                <Identifier xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns2:SubjectIdentifierByCompanyType">
                    <ns2:Identifier>{nip}</ns2:Identifier>
                </Identifier>
                <DocumentType>
                    <ns2:Service>KSeF</ns2:Service>
                    <ns2:FormCode>
                        <ns2:SystemCode>FA (2)</ns2:SystemCode>
                        <ns2:SchemaVersion>1-0E</ns2:SchemaVersion>
                        <ns2:TargetNamespace>http://crd.gov.pl/wzor/2023/06/29/12648/</ns2:TargetNamespace>
                        <ns2:Value>FA</ns2:Value>
                    </ns2:FormCode>
                </DocumentType>
                <Token>{encrypted_token}</Token>
            </ns3:Context>
        </ns3:InitSessionTokenRequest>'''
    response = requests.post(url,body,headers=headers)
    print(response.status_code)
    if response.status_code > 200 and response.status_code < 300:
        return response.json()['sessionToken']['token']
    else:
        print(response.content)
        raise RuntimeError
    
def session_status(session_token, host = HOST):
    url = f'https://{host}.mf.gov.pl/api/online/Session/Status?PageSize=100&PageOffset=0&IncludeDetails=true'
    headers = {
        "SessionToken": session_token,
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        raise RuntimeError

if __name__== '__main__':
    session_token = init_token(*get_encrypted_token_and_challenge())
    session_status(session_token)
    
