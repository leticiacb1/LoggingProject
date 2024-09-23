import typing 

def say_hello(event, context) -> typing.Dict[str, str]:
    '''
    Handler Function
    '''
    return {
        "created_by": "your name",
        "message": "Hello World!"
    }