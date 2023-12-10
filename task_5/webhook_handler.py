from fastapi import FastAPI, Header, Request, status, HTTPException
from task_5.functions_to_call import function2
from task_5.functions_to_call import function1
import uvicorn
import json

from config import settings
from webhook_validation import generate_hash_signature

app = FastAPI()


@app.post('/Datalore', status_code=status.HTTP_202_ACCEPTED)
async def webhook(request: Request, x_hub_signature: str = Header(None)):
    payload = await request.body()
    secret = settings.WEBHOOK_SECRET.encode('utf-8')
    signature = generate_hash_signature(secret, payload)
    print(f'sha1={signature}')
    if x_hub_signature != f'sha1={signature}':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Error while authenticating the signature'
        )
    # get function field from payload and check its value
    data = json.loads(payload)
    function_name = data.get('function')
    if function_name == 'function1':
        # Call function 1
        result = function1()
    elif function_name == 'function2':
        # Call function 2
        result = function2()
    else:
        # Wrong function name
        result = {'error': 'Invalid function'}
    return result


if __name__ == '__main__':
    uvicorn.run('webhook_handler:app', reload=True)
