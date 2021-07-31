# treble.ai's technical test v1.1.3 - Part 2

This is a serverless project, refer to the [serverless installation guide](https://www.serverless.com/framework/docs/providers/aws/guide/installation/) to resolve the requirements needed to run this project. It is not needed that the project is deployed to the cloud. It is enough that the project runs locally, please use the [serverless offline plugin](https://www.npmjs.com/package/serverless-offline) to achieve this.

Once everything is setup correctly. You should be able to run:

```bash
$ serverless offline
```

And get something like this:

```bash
offline: Starting Offline: dev/us-east-1.
offline: Offline [http for lambda] listening on http://localhost:3002

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   POST | http://localhost:3000/dev/spellcheck                           │
   │   POST | http://localhost:3000/2015-03-31/functions/hello/invocations   │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘

offline: [HTTP] server ready: http://localhost:3000 🚀
offline: 
offline: Enter "rp" to replay the last request

offline: POST /dev/spellcheck (λ: hello)
```

To test that the endpoint is working correctly use cURL:

```bash
$ curl http://localhost:3000/dev/spellcheck> -X POST -d '{ "text": "un lgar para la hopinion"}'
{ "text" : "un lugar para la opinión" }
```
