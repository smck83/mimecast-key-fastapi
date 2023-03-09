# mimecast-key-fastapi
Generate Mimecast MC tokens

A API endpoint using FastAPI to generate Mimecast API tokens.

Where you are looking to leverage Microsoft Flow, Logic Apps or Power Automate you can pass y


http://apphostname:8000/generate-mc-token/{application_key}/?uri=/api/account/get-account&access_key={access_key}&secret_key={secret_key}

Sample response:
`{"mc-token":"MC mYtOL3XZCOwG96BOiFTZRsyIKyobj_W1HOLw0NUpt30V-n2hQVzAU365AH5bmOjWCqUU8Mg6Q2cCCdZrZ2zZ5zv1-QP_6YT2k1Jc3BZFR4UKMnnbtOUHI4Wdx-30G1FtuwmGtJxmAZ8htHNB8QCJLg:3qNC6VFZG3Uy0Nn05/6Qst2q/ss=","uri":"/api/account/get-account","request-id":"0fa14008-be6c-47d8-aa55-5c438e8c09ea","request-date":"Thu, 09 Mar 2023 09:29:26 UTC"}1
