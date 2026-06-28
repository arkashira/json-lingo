 # Tech-Spec.md

## Stack
- Language: TypeScript for type safety and compatibility with Node.js and browser environments.
- Framework: Next.js for server-side rendering and React for user interface.
- Runtime: Node.js for server-side execution and Deno for client-side execution (for better security).

## Hosting
- Free-Tier-First: Host on AWS Amplify for the first 12 months, leveraging their free tier to minimize initial costs.
- Specific Platforms: Support deployment on AWS Elastic Beanstalk, Heroku, and Vercel for flexibility and ease of deployment for users.

## Data Model
- Tables/Collections:
  - Translations: ID, JSON data, source language, target language, timestamp, status (pending, in-progress, completed).
  - Users: ID, username, password (hashed), email, role (free, pro).
  - API Keys: ID, user ID, key, created_at, updated_at.

- Key Fields:
  - Translations: ID, source language, target language.
  - Users: ID, email.
  - API Keys: ID, user ID.

## API Surface
- Endpoints (RESTful API):
  1. POST /api/auth/register: Register a new user.
  2. POST /api/auth/login: Login a user.
  3. GET /api/translations: Retrieve a list of translations.
  4. POST /api/translations: Create a new translation job.
  5. GET /api/translations/:id: Retrieve a specific translation.
  6. PUT /api/translations/:id: Update a specific translation.
  7. DELETE /api/translations/:id: Delete a specific translation.
  8. GET /api/translations/status/:status: Retrieve translations with a specific status.
  9. GET /api/translations/user/:userId: Retrieve translations for a specific user.
  10. GET /api/translations/language/:sourceLanguage/:targetLanguage: Retrieve translations for a specific source and target language.

## Security Model
- Auth: Implement JWT-based authentication for API access.
- Secrets: Store sensitive data (API keys, database credentials) in AWS Secrets Manager.
- IAM: Implement IAM roles for service accounts to manage access to AWS resources.

## Observability
- Logs: Use AWS CloudWatch for server-side logs and Sentry for client-side logs.
- Metrics: Use AWS CloudWatch for monitoring key metrics such as request rate, error rate, and latency.
- Traces: Use AWS X-Ray for distributed tracing to identify and troubleshoot performance issues.

## Build/CI
- Use AWS CodePipeline for continuous integration and deployment, with GitHub as the source repository.
- Use AWS CodeBuild for building and testing the application.
- Use AWS CodeDeploy for deploying the application to the chosen platform.
- Use AWS CodeCommit (optional) for private repository hosting.