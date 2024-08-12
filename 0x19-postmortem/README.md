# Postmortem: Rust Server Deployment Outage

## Issue Summary
**Duration:** August 10, 2024, 14:00 - 16:30 UTC (2 hours 30 minutes)  
**Impact:** The primary service affected was our API server, causing 75% of users to experience 500 Internal Server Errors when attempting to access the application. Affected users were unable to retrieve or submit data, severely impacting the user experience.  
**Root Cause:** The outage was caused by deploying a Rust server with altered database migration files that mismatched with the schema already migrated in the PostgreSQL database.

## Timeline
- **14:00 UTC:** Issue detected by automated monitoring, which reported a spike in 500 Internal Server Errors.
- **14:05 UTC:** Engineers received alerts and began investigating the issue. Initial suspicion was a network or load balancer problem due to the sudden spike.
- **14:15 UTC:** Investigation focused on the database as queries were failing. The assumption was that the database was under high load or had corrupted indexes.
- **14:30 UTC:** Misleading debugging paths explored included checking for network partition and load balancing issues, both ruled out after 30 minutes.
- **15:00 UTC:** Escalation to the DevOps team, who then examined the most recent deployment logs.
- **15:20 UTC:** It was discovered that the latest deployment included altered database migration files that were inconsistent with the existing PostgreSQL schema.
- **15:45 UTC:** Engineers rolled back the deployment to the previous stable version, which restored the service.
- **16:30 UTC:** Service fully restored, and all users could access the application without issues.

## Root Cause and Resolution
**Root Cause:** The root cause of the outage was the deployment of a Rust server that included altered database migration files. These files conflicted with the existing schema in the PostgreSQL database. Specifically, some column names were changed, and certain constraints were altered, which caused the server to fail when trying to execute queries against the database.

**Resolution:** The issue was resolved by rolling back the deployment to the previous stable version, which used the correct database schema. After the rollback, all services returned to normal operation. Post-rollback, the team reviewed the migration files to ensure they aligned with the existing schema before planning a correct redeployment.

## Corrective and Preventative Measures
**Improvements and Fixes:**
- Implement a strict review process for database migration files before deployment to ensure compatibility with the existing schema.
- Enhance monitoring to include schema validation checks during the deployment process.
- Introduce automated testing that includes migration scenarios to catch issues before they reach production.

**TODO List:**
1. Patch the migration tool to include schema validation against the current database state.
2. Add automated tests for database migrations in the CI/CD pipeline.
3. Implement additional monitoring to detect schema mismatches during the deployment.
4. Document the migration process, emphasizing the importance of maintaining schema consistency.
5. Train the development team on best practices for handling database migrations and the potential risks of altering schema files.

By addressing these areas, we aim to prevent similar issues in the future and ensure a more reliable deployment process.

