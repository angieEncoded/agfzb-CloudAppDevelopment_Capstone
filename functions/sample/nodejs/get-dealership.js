const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');
require('dotenv').config()

// GEt from env variables for testing
const params = {
    IAM_API_KEY: process.env.IAM_API_KEY,
    COUCH_URL: process.env.COUCH_URL
}

// console.log(params.IAM_API_KEY)

async function main(params) {
    // console.log(params)
    const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
    const cloudant = CloudantV1.newInstance({
        authenticator: authenticator
    });

    cloudant.setServiceUrl(params.COUCH_URL);
    try {
        let dbList = await cloudant.postAllDocs({
            db: 'dealerships',
            includeDocs: true,
        });
        console.log(dbList.result)
        return { "body": dbList.result };
    } catch (error) {
        return { error: error.description };
    }
}

// invoke for testing
main(params)