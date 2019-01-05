#/usr/bin/bash
curl -XPOST "http://10.0.37.237:8080/usermanager/validuser" -d'{"userName":"admin","password":"28E0C3732464399B04C27D8600E870C9"}' --cookie-jar cookie_file
curl -XPOST "http://10.0.37.237:8080/DatasetManager/createDataset" -d '{
	"owner": "admin",
	"replication": "0",
	"schema": {
		"properties": [{
			"fieldName": "time",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "batch_no",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "track_target_kind",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "track_target_type",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "attribute",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "nationality",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "order",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "dynamic",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "high",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "longitude",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "latitude",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "distance_x",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "distance_y",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "velocity_x",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "velocity_y",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "track_time",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "bearing",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "velocity_h",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "threat_cla",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "threat_time",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "battle_state",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		},
		{
			"fieldName": "flag",
			"name": "",
			"index": "not_analyzed",
			"store": "true",
			"type": "string",
			"key": "false"
		}]
	},
	"visable": "public",
	"isPartition": "false",
	"datasetName": "bdtaishi_tytsmb",
	"shard": "3"}' -b ./cookie_file