
exports.lambdaHandler = async (event, context) => {
    return event.data;
};


//sam local invoke -e ./lambda/lambda_event.json LambdaDemoFunction  


//PROMPT='%B%F{green}%1~%f $ %b'

//sam local invoke -e ./awsWafIpSet/apigateway_event.json AwsWafIpSet

//sam local start-api 


//sam build --use-container --container-env-var-file env_vars.json

//sam local start-api --env-vars env_vars.json 

//sam deploy --guided



