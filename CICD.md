# CI/CD

 1. Architectural Overview
   * Automation Runner: tox manages the test environments and execution (defined in tox.ini).
   * Orchestration: Jenkinsfile defines the CI pipeline (Linting -> Testing).
   * Job Provisioning: Jenkins Job Builder (jjb/mydiary.yaml) manages the "Multibranch Pipeline" job in Jenkins.

  2. Setup Steps


  A. Prepare the Jenkins Server
  Ensure your Jenkins instance has the following plugins installed:
   * GitHub Branch Source Plugin: Essential for Multibranch Pipelines to discover PRs.
   * Pipeline Plugin: To execute the Jenkinsfile.


  B. Configure Jenkins Credentials
  Add a "Username with password" (using a GitHub Personal Access Token) in Jenkins with the ID github-token, as referenced in jjb/mydiary.yaml.

  C. Deploy the Jenkins Job
  Use the provided JJB configuration to create the job on your Jenkins server.
   1 # From the project root
   2 jenkins-jobs --conf jjb/jenkins_jobs.ini update jjb/mydiary.yaml


  D. Configure GitHub Webhooks
  To trigger tests instantly on every PR:
   1. In your GitHub repository, go to Settings > Webhooks.
   2. Add a webhook pointing to http://<your-jenkins-url>/github-webhook/.
   3. Select "Let me select individual events" and check Pushes and Pull requests.


  3. How the PR Workflow Works
   1. Detection: When a PR is opened, Jenkins detects the new branch/PR via the webhook.
   2. Execution: Jenkins pulls the code and runs the stages defined in the Jenkinsfile:
       * tox -e lint: Runs ruff for code quality.
       * tox -e py3: Runs pytest with coverage.
   3. Feedback: The build status (Success/Failure) is reported back to the GitHub PR interface.


  4. Local Validation
  Before pushing changes, you can verify that the CI logic works locally by running:
   1 tox
  This will run both the linting and testing suites exactly as they will run in the CI environment.

