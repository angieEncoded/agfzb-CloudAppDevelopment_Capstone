"""Get review testing code"""
import os
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

ibm_params = {
    "IAM_API_KEY": os.getenv("IAM_API_KEY"),
    "COUCH_URL": os.getenv("COUCH_URL"),
    "dealer_id": "15"
}
        
def main(dict):
    """Get review testing code"""
    authenticator = IAMAuthenticator(dict["IAM_API_KEY"])
    service = CloudantV1(authenticator = authenticator)
    service.set_service_url(dict["COUCH_URL"])
    response = service.post_find(
        db="reviews",
        selector={"dealership": {"$eq": int(dict["dealer_id"])}},
    ).get_result()
    try:
        result={
            'headers': {'Content-Type':'application/json'}, 
            'body': {'data':response}
        }
        return result
    except Exception as e:
        return{
            "statusCode": 404,
            "message": "Something went wrong"
        }

main(ibm_params)
