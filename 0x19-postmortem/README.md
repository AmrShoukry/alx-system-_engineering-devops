### Issue Summary
The outage occurred from 1:17 PM on October 7, 2023, until 2:39 PM on October 7, 2023, in the +3 GMT timezone.
The "Favourits" feature experienced service disruptions during the outage, causing it to not work properly. Approximately 36% of users were affected by this issue.
The root cause of the issue was that the database was not updated when someone pressed the "Add to Favorites" button. This failure to update the database led to the malfunction of the "Favourites" feature during the outage.

### Timeline
* 12:48 PM - The "Add to Favorites" feature was deployed to production.
* 01:17 PM - The problem of failing to update the favorites list was identified.
* 01:18 PM - The issue was detected when numerous customers reported that the "Add to Favorites" button was not functioning as anticipated.
* 01:19 PM - The incident was escalated to the backend team.
* 01:35 PM - The backend team received a notification about an issue with their recently implemented feature.
* 01:43 PM - The backend team indicated that everything appeared to be in order on their end, suggesting that the issue might be related to users' internet connections.
* 02:39 PM - The backend team resolved the incident by opting to rollback the feature's functionality until they could identify and address the underlying issue.

### Root cause and resolution 
The root cause of the problem was a semantic error in the code of the new feature. This error prevented the database from being updated properly when a user clicked the "Add to Favorites" button. As a result, the user's favorites table in the database remained empty, even if the user had clicked the "Add to Favorites" button for multiple products. Essentially, the code logic for updating the database was flawed, leading to the persistence of an empty favorites table despite user interactions with the feature.
To address the problem, the solution involved temporarily removing the favorites feature from the system. This action was taken to allow for a thorough investigation of the bug causing the issue for users. Subsequently, the team decided to roll back the most recent changes made to the system. By doing so, they effectively reverted the code and configurations to a previous state, where the feature was functioning correctly. This rollback served as a temporary fix until the specific bug responsible for the problem could be identified and resolved.

### Corrective and preventative measures
There is room for improvement in ensuring that any new feature undergoes thorough testing before its deployment to the production environment. Specifically, new features should not be approved for production release if they lack proper unit testing.
To tackle current or potential issues, a set of tasks should be undertaken (Implement unit testing, Deploy a monitoring tool).
