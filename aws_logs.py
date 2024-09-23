from dataclass.compress import CompressFile
from dataclass.lambda_function import LambdaFunction
from dataclass.logs import Logs
import time

# Variaveis
lambda_filename = "hello.py"
lambda_compress = "hello.zip"

lambda_function_name = "say_hello"   # Change Function Name in AWS Lambda
handler_function_name = "say_hello"  # Funcion name in file hello.py
username = "leticiacb1"

handler = lambda_filename.split('.')[0] + "." + handler_function_name
function_name = lambda_function_name + "_" + username 

lambda_group_name = f"/aws/lambda/{function_name}"
try : 
    # Compress
    compress = CompressFile()
    compress.run(lambda_filename=lambda_filename, compress_filename=lambda_compress)

    # Instantiate Lambda Function
    _lambda = LambdaFunction()
    _lambda.create_client()
    _lambda.read_function(compress_filename=lambda_compress)
    _lambda.create_function(function_handler= handler, function_name=function_name)

    time.sleep(1) # Wait lambda function to be deployed

    _lambda.check_function(function_name=function_name)

    # CloudWatch Logs:
    logs = Logs()
    logs.create_client()
    logs.get_events(lambda_group_name= lambda_group_name)

except Exception as e:
    print(f"\n    [ERROR] An error occurred in main process: \n {e} \n")

finally:
    # Cleaning:
    _lambda.cleanup(function_name=function_name)