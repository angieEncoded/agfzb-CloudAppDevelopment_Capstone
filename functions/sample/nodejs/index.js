/**
 * Get all databases
 */

const { CloudantV1 } = require("@ibm-cloud/cloudant");
const { IamAuthenticator } = require("ibm-cloud-sdk-core");

function main(params) {
  const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY });
  const cloudant = CloudantV1.newInstance({
    authenticator: authenticator,
  });
  cloudant.setServiceUrl(params.COUCH_URL);

  let dbList = getDbs(cloudant);
  return { dbs: dbList };
}

function getDbs(cloudant) {
  cloudant.getAllDbs()
    .then((body) => {
      body.forEach((db) => {
        dbList.push(db);
      });
    })
    .catch((err) => {
      console.log(err);
    });
}
// commenting this out, it's just a scratchpad anyways
// if (params.dealer_id) {
//   try {
//     let dbList = await cloudant.postFind({
//       db: 'dealerships',
//       "selector": {
//         "id": params.dealer_id
//       }
//     });
//     return { "body": dbList.result };
//   } catch (error) {
//     return { error: error.description };
//   }
// }

// if (params.state) {
//   try {
//     let dbList = await cloudant.postFind({
//       db: 'dealerships',
//       "selector": {
//         "st": params.state
//       }
//     });
//     return { "body": dbList.result };
//   } catch (error) {
//     return { error: error.description };
//   }
// }
