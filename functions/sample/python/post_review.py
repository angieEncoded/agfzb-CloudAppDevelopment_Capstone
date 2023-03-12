# Commenting out my scratchpad, the linter is going crazy
# import sys
# import os
# from ibmcloudant.cloudant_v1 import CloudantV1
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# from dotenv import load_dotenv

# load_dotenv()

# review = {
# "review":
#     {
#         "id": 1114,
#         "name": "Upkar Lidder",
#         "dealership": 15,
#         "review": "Great service!",
#         "purchase": False,
#         "another": "field",
#         "purchase_date": "02/16/2021",
#         "car_make": "Audi",
#         "car_model": "Car",
#         "car_year": 2021
#     }
# }

# dict = {
#     "IAM_API_KEY": os.getenv("IAM_API_KEY"),
#     "COUCH_URL": os.getenv("COUCH_URL"),
#     "review": review
# }

# def main(dict):
#     authenticator = IAMAuthenticator(dict["IAM_API_KEY"])
#     service = CloudantV1(authenticator = authenticator)
#     service.set_service_url(dict["COUCH_URL"])
#     response = service.post_document(db='reviews', document=dict["review"]).get_result()
#     try:
#     # result_by_filter=my_database.get_query_result(selector,raw_result=True)
#         result= {
#         'headers': {'Content-Type':'application/json'},
#         'body': {'data':response}
#         }
#         return result
#     except:
#         return {
#         'statusCode': 404,
#         'message': 'Something went wrong'
#         }

# main(dict)
