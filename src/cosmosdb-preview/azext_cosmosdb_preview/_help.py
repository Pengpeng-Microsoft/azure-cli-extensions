# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import


helps['cosmosdb create'] = """
type: command
short-summary: Create a new Azure Cosmos DB database account.
parameters:
  - name: --locations
    short-summary: Add a location to the Cosmos DB database account
    long-summary: |
        Usage:          --locations KEY=VALUE [KEY=VALUE ...]
        Required Keys:  regionName, failoverPriority
        Optional Key:   isZoneRedundant
        Default:        single region account in the location of the specified resource group.
        Failover priority values are 0 for write regions and greater than 0 for read regions. A failover priority value must be unique and less than the total number of regions.
        Multiple locations can be specified by using more than one `--locations` argument.
  - name: --databases-to-restore
    short-summary: Add a database and its collection names to restore
    long-summary: |
        Usage:          --databases-to-restore name=DatabaseName collections=collection1 [collection2 ...]
examples:
  - name: Create a new Azure Cosmos DB database account.
    text: az cosmosdb create --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --subscription MySubscription
  - name: Create a new Azure Cosmos DB database account with two regions. UK South is zone redundant.
    text: az cosmosdb create -n myaccount -g mygroup --locations regionName=eastus failoverPriority=0 isZoneRedundant=False --locations regionName=uksouth failoverPriority=1 isZoneRedundant=True --enable-multiple-write-locations
  - name: Create a new Azure Cosmos DB database account by restoring from an existing account in the given location
    text: az cosmosdb create -n restoredaccount -g mygroup --is-restore-request true --restore-source /subscriptions/2296c272-5d55-40d9-bc05-4d56dc2d7588/providers/Microsoft.DocumentDB/locations/westus/restorableDatabaseAccounts/d056a4f8-044a-436f-80c8-cd3edbc94c68 --restore-timestamp 2020-07-13T16:03:41+0000 --locations regionName=westus failoverPriority=0 isZoneRedundant=False
"""

helps['cosmosdb restore'] = """
type: command
short-summary: Create a new Azure Cosmos DB database account by restoring from an existing database account.
parameters:
  - name: --databases-to-restore
    short-summary: Add a database and its collection names to restore
    long-summary: |
        Usage:          --databases-to-restore name=DatabaseName collections=collection1 [collection2 ...]
        Multiple databases can be specified by using more than one `--databases-to-restore` argument.
examples:
  - name: Create a new Azure Cosmos DB database account by restoring from an existing database account.
    text: az cosmosdb restore --target-database-account-name MyRestoredCosmosDBDatabaseAccount --account-name MySourceAccount --restore-timestamp 2020-07-13T16:03:41+0000 -g MyResourceGroup --location westus
  - name: Create a new Azure Cosmos DB database account by restoring only the selected databases and collections from an existing database account.
    text: az cosmosdb restore -g MyResourceGroup --target-database-account-name MyRestoredCosmosDBDatabaseAccount --account-name MySourceAccount --restore-timestamp 2020-07-13T16:03:41+0000 --location westus --databases-to-restore name=MyDB1 collections=collection1 collection2 --databases-to-restore name=MyDB2 collections=collection3 collection4
"""

helps['cosmosdb update'] = """
type: command
short-summary: Update an Azure Cosmos DB database account.
parameters:
  - name: --locations
    short-summary: Add a location to the Cosmos DB database account
    long-summary: |
        Usage:          --locations KEY=VALUE [KEY=VALUE ...]
        Required Keys:  regionName, failoverPriority
        Optional Key:   isZoneRedundant
        Default:        single region account in the location of the specified resource group.
        Failover priority values are 0 for write regions and greater than 0 for read regions. A failover priority value must be unique and less than the total number of regions.
        Multiple locations can be specified by using more than one `--locations` argument.
examples:
  - name: Update an Azure Cosmos DB database account.
    text: az cosmosdb update --capabilities EnableGremlin --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
  - name: Update an new Azure Cosmos DB database account with two regions. UK South is zone redundant.
    text: az cosmosdb update -n myaccount -g mygroup --locations regionName=eastus failoverPriority=0 isZoneRedundant=False --locations regionName=uksouth failoverPriority=1 isZoneRedundant=True --enable-multiple-write-locations
  - name: Update the backup policy parameters of a database account with Periodic backup type.
    text: az cosmosdb update -n myaccount -g mygroup --backup-interval 240 --backup-retention 24
"""

helps['cosmosdb restorable-database-account'] = """
type: group
short-summary: Manage restorable Azure Cosmos DB accounts.
"""

helps['cosmosdb restorable-database-account list'] = """
type: command
short-summary: List all the database accounts that can be restored.
"""

helps['cosmosdb restorable-database-account show'] = """
type: command
short-summary: Show the details of a database account that can be restored.
"""

helps['cosmosdb sql restorable-database'] = """
type: group
short-summary: Manage different versions of sql databases that are restorable in a Azure Cosmos DB account.
"""

helps['cosmosdb sql restorable-database list'] = """
type: command
short-summary: List all the versions of all the sql databases that were created / modified / deleted in the given restorable account.
"""

helps['cosmosdb sql restorable-container'] = """
type: group
short-summary: Manage different versions of sql containers that are restorable in a database of a Azure Cosmos DB account.
"""

helps['cosmosdb sql restorable-container list'] = """
type: command
short-summary: List all the versions of all the sql containers that were created / modified / deleted in the given database and restorable account.
"""

helps['cosmosdb sql restorable-resource'] = """
type: group
short-summary: Manage the databases and its containers that can be restored in the given account at the given timesamp and region.
"""

helps['cosmosdb sql restorable-resource list'] = """
type: command
short-summary: List all the databases and its containers that can be restored in the given account at the given timesamp and region.
"""

helps['cosmosdb mongodb restorable-database'] = """
type: group
short-summary: Manage different versions of mongodb databases that are restorable in a Azure Cosmos DB account.
"""

helps['cosmosdb mongodb restorable-database list'] = """
type: command
short-summary: List all the versions of all the mongodb databases that were created / modified / deleted in the given restorable account.
"""

helps['cosmosdb mongodb restorable-collection'] = """
type: group
short-summary: Manage different versions of mongodb collections that are restorable in a database of a Azure Cosmos DB account.
"""

helps['cosmosdb mongodb restorable-collection list'] = """
type: command
short-summary: List all the versions of all the mongodb collections that were created / modified / deleted in the given database and restorable account.
"""

helps['cosmosdb mongodb restorable-resource'] = """
type: group
short-summary: Manage the databases and its collections that can be restored in the given account at the given timesamp and region.
"""

helps['cosmosdb mongodb restorable-resource list'] = """
type: command
short-summary: List all the databases and its collections that can be restored in the given account at the given timesamp and region.
"""

helps['cosmosdb sql role'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL role resources.
"""

helps['cosmosdb sql role definition'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL role definitions.
"""

helps['cosmosdb sql role definition create'] = """
type: command
short-summary: Create a SQL role definition under an Azure Cosmos DB account.
examples:
  - name: Create a SQL role definition under an Azure Cosmos DB account using a JSON string.
    text: |
      az cosmosdb sql role definition create --account-name MyAccount --resource-group MyResourceGroup --body '{
        "Id": "be79875a-2cc4-40d5-8958-566017875b39",
        "RoleName": "My Read Only Role",
        "Type": "CustomRole",
        "AssignableScopes": ["/dbs/mydb/colls/mycontainer"],
        "Permissions": [{
          "DataActions": [
            "Microsoft.DocumentDB/databaseAccounts/readMetadata",
            "Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/items/read",
            "Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/executeQuery",
            "Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/readChangeFeed"
          ]
        }]
      }'
  - name: Create a SQL role definition under an Azure Cosmos DB account using a JSON file.
    text: az cosmosdb sql role definition create --account-name MyAccount --resource-group MyResourceGroup --body @role-definition.json
"""

helps['cosmosdb sql role definition delete'] = """
type: command
short-summary: Delete a SQL role definition under an Azure Cosmos DB account.
examples:
  - name: Create a SQL role definition under an Azure Cosmos DB account.
    text: az cosmosdb sql role definition delete --account-name MyAccount --resource-group MyResourceGroup --id be79875a-2cc4-40d5-8958-566017875b39
"""

helps['cosmosdb sql role definition exists'] = """
type: command
short-summary: Check if an Azure Cosmos DB role definition exists.
examples:
  - name: Check if an Azure Cosmos DB role definition exists.
    text: az cosmosdb sql role definition exists --account-name MyAccount --resource-group MyResourceGroup --id be79875a-2cc4-40d5-8958-566017875b39
"""

helps['cosmosdb sql role definition list'] = """
type: command
short-summary: List all SQL role definitions under an Azure Cosmos DB account.
examples:
  - name: List all SQL role definitions under an Azure Cosmos DB account.
    text: az cosmosdb sql role definition list --account-name MyAccount --resource-group MyResourceGroup
"""

helps['cosmosdb sql role definition show'] = """
type: command
short-summary: Show the properties of a SQL role definition under an Azure Cosmos DB account.
examples:
  - name: Show the properties of a SQL role definition under an Azure Cosmos DB account.
    text: az cosmosdb sql role definition show --account-name MyAccount --resource-group MyResourceGroup --id be79875a-2cc4-40d5-8958-566017875b39
"""

helps['cosmosdb sql role definition update'] = """
type: command
short-summary: Update a SQL role definition under an Azure Cosmos DB account.
examples:
  - name: Update a SQL role definition under an Azure Cosmos DB account.
    text: az cosmosdb sql role definition update --account-name MyAccount --resource-group MyResourceGroup --body @role-definition.json
"""

helps['cosmosdb sql role assignment'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL role assignments.
"""

helps['cosmosdb sql role assignment create'] = """
type: command
short-summary: Create a SQL role assignment under an Azure Cosmos DB account.
examples:
  - name: Create a SQL role assignment under an Azure Cosmos DB account.
    text: |
      az cosmosdb sql role assignment create --account-name MyAccount --resource-group MyResourceGroup \\
        --role-assignment-id cb8ed2d7-2371-4e3c-bd31-6cc1560e84f8 \\
        --role-definition-id be79875a-2cc4-40d5-8958-566017875b39 \\
        --scope "/dbs/mydb/colls/mycontainer" \\
        --principal-id 6328f5f7-dbf7-4244-bba8-fbb9d8066506
"""

helps['cosmosdb sql role assignment delete'] = """
type: command
short-summary: Delete a SQL role assignment under an Azure Cosmos DB account.
examples:
  - name: Delete a SQL role assignment under an Azure Cosmos DB account.
    text: az cosmosdb sql role assignment delete --account-name MyAccount --resource-group MyResourceGroup --role-assignment-id cb8ed2d7-2371-4e3c-bd31-6cc1560e84f8
"""

helps['cosmosdb sql role assignment exists'] = """
type: command
short-summary: Check if an Azure Cosmos DB role assignment exists.
examples:
  - name: Check if an Azure Cosmos DB role assignment exists.
    text: az cosmosdb sql role assignment exists --account-name MyAccount --resource-group MyResourceGroup --role-assignment-id cb8ed2d7-2371-4e3c-bd31-6cc1560e84f8
"""

helps['cosmosdb sql role assignment list'] = """
type: command
short-summary: List all SQL role assignments under an Azure Cosmos DB account.
examples:
  - name: List all SQL role assignments under an Azure Cosmos DB account.
    text: az cosmosdb sql role assignment list --account-name MyAccount --resource-group MyResourceGroup
"""

helps['cosmosdb sql role assignment show'] = """
type: command
short-summary: Show the properties of a SQL role assignment under an Azure Cosmos DB account.
examples:
  - name: Show the properties of a SQL role assignment under an Azure Cosmos DB account.
    text: az cosmosdb sql role assignment show --account-name MyAccount --resource-group MyResourceGroup --role-assignment-id cb8ed2d7-2371-4e3c-bd31-6cc1560e84f8
"""

helps['cosmosdb sql role assignment update'] = """
type: command
short-summary: Update a SQL role assignment under an Azure Cosmos DB account.
examples:
  - name: Update a SQL role assignment under an Azure Cosmos DB account.
    text: |
      az cosmosdb sql role assignment update --account-name MyAccount --resource-group MyResourceGroup \\
        --role-assignment-id cb8ed2d7-2371-4e3c-bd31-6cc1560e84f8 \\
        --role-definition-id updated-role-definition-id
"""
