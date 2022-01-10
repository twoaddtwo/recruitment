import login
import requests
import json


def create_zhongyaoyinpian():
    url = "https://test.igancao.cn:8000/gateway/treatment/cloudRecipel/creatCloudRecipel"
    headers = login.headers
    data = {
	"sort": 1,
	"prescriptionId": 2782,
	"dfId": 101,
	"dsId": 1,
	"medicineList": [{
		"id": 281,
		"quantity": 1,
		"brief": ""
	}],
	"ctmExt": {
		"amount": 7,
		"bolusSpec": "",
		"concentrationPackageAmount": "",
		"concentrationPackageNotes": "",
		"dose": 1,
		"isApplyPowder": 0,
		"isCapsulePowder": 0,
		"isCream": 0,
		"isCreamGranule": 0,
		"isDecoct": 1,
		"isDrychip": 0,
		"isExtract": 0,
		"isExtractGranule": 0,
		"isFeetPowder": 0,
		"isMaskPowder": 0,
		"isSachetPowder": 0,
		"isSwallowPowder": 0,
		"isTeaPowder": 0,
		"isPillowPowder": 0,
		"packType": "",
		"pillType": "",
		"takeDays": 1,
		"usageMode": "ORAL",
		"powderPackageAmountTip": "",
		"packageTypeName": ""
	},
	"doctAdvice": {
		"notesDoctor": "",
		"others": "",
		"taboo": "",
		"usageBrief": "",
		"usageMethod": "200ml每包，一天2次",
		"usageTime": "饭后半小时"
	},
	"from": 0
}
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(r.json())
    return r.json()['data']

def create_nongsuowan():
	url = "https://test.igancao.cn:8000/gateway/treatment/cloudRecipel/creatCloudRecipel"
	headers = login.headers
	data = {
	"sort": 4,
	"prescriptionId": 2782,
	"dfId": 102,
	"dsId": 1,
	"medicineList": [{
		"id": 269,
		"quantity": 1000,
		"brief": ""
	}],
	"ctmExt": {
		"amount": 1,
		"bolusSpec": "",
		"concentrationPackageAmount": "",
		"concentrationPackageNotes": "",
		"dose": 5,
		"isApplyPowder": 0,
		"isCapsulePowder": 0,
		"isCream": 0,
		"isCreamGranule": 0,
		"isDecoct": "",
		"isDrychip": 0,
		"isExtract": 0,
		"isExtractGranule": 0,
		"isFeetPowder": 0,
		"isMaskPowder": 0,
		"isSachetPowder": 0,
		"isSwallowPowder": 0,
		"isTeaPowder": 0,
		"isPillowPowder": 0,
		"packType": "",
		"pillType": "WATER",
		"takeDays": 27,
		"timesPerDay": 3,
		"usageMode": "",
		"powderPackageAmountTip": "",
		"packageTypeName": ""
	},
	"doctAdvice": {
		"notesDoctor": "",
		"others": "",
		"taboo": "",
		"usageBrief": "",
		"usageMethod": "每天3次,每次5g",
		"usageTime": "饭后半小时"
	},
	"from": 0
}
	r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
	print(r.json())
	return r.json()['data']

def create_keliji():
	url = "https://test.igancao.cn:8000/gateway/treatment/cloudRecipel/creatCloudRecipel"
	headers = login.headers
	data = {
	"sort": 5,
	"prescriptionId": 2782,
	"dfId": 103,
	"dsId": 3,
	"medicineList": [{
		"id": 270,
		"quantity": 2000,
		"brief": ""
	}],
	"ctmExt": {
		"amount": 7,
		"bolusSpec": "",
		"concentrationPackageAmount": "",
		"concentrationPackageNotes": "",
		"dose": 1,
		"isApplyPowder": 0,
		"isCapsulePowder": 0,
		"isCream": 0,
		"isCreamGranule": 0,
		"isDecoct": "",
		"isDrychip": 0,
		"isExtract": 0,
		"isExtractGranule": 0,
		"isFeetPowder": 0,
		"isMaskPowder": 0,
		"isSachetPowder": 0,
		"isSwallowPowder": 0,
		"isTeaPowder": 0,
		"isPillowPowder": 0,
		"packType": "",
		"pillType": "",
		"takeDays": 1,
		"usageMode": "ORAL",
		"powderPackageAmountTip": "",
		"packageTypeName": ""
	},
	"doctAdvice": {
		"notesDoctor": "",
		"others": "",
		"taboo": "",
		"usageBrief": "",
		"usageMethod": "一天2次",
		"usageTime": ""
	},
	"from": 0
}
	r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
	print(r.json())
	return r.json()['data']

def create_fenji():
	url = "https://test.igancao.cn:8000/gateway/treatment/cloudRecipel/creatCloudRecipel"
	headers = login.headers
	data = {
	"sort": 6,
	"prescriptionId": 2782,
	"dfId": 104,
	"dsId": 2,
	"medicineList": [{
		"id": 750,
		"quantity": 1000,
		"brief": ""
	}],
	"ctmExt": {
		"amount": 1,
		"bolusSpec": "",
		"concentrationPackageAmount": "",
		"concentrationPackageNotes": "",
		"dose": "15",
		"isApplyPowder": 0,
		"isCapsulePowder": 0,
		"isCream": 0,
		"isCreamGranule": 0,
		"isDecoct": "",
		"isDrychip": 0,
		"isExtract": 0,
		"isExtractGranule": 0,
		"isFeetPowder": 0,
		"isMaskPowder": 0,
		"isSachetPowder": 0,
		"isSwallowPowder": 0,
		"isTeaPowder": 1,
		"isPillowPowder": 0,
		"packType": "ORDINARY",
		"pillType": "",
		"takeDays": 1,
		"timesPerDay": 3,
		"usageMode": "ORAL",
		"powderPackageAmountTip": "约63～65包",
		"packageTypeName": "茶包(约5-8目)"
	},
	"doctAdvice": {
		"notesDoctor": "",
		"others": "",
		"taboo": "",
		"usageBrief": "",
		"usageMethod": "每天3次,每次15g",
		"usageTime": "饭后半小时"
	},
	"from": 0
}
	r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
	print(r.json())
	return r.json()['data']

def create_damiwan():
	url = "https://test.igancao.cn:8000/gateway/treatment/cloudRecipel/creatCloudRecipel"
	headers = login.headers
	data = {
	"sort": 7,
	"prescriptionId": 2782,
	"dfId": 105,
	"dsId": 11,
	"medicineList": [{
		"id": 281,
		"quantity": 1000,
		"brief": ""
	}],
	"ctmExt": {
		"amount": 1,
		"bolusSpec": "3g",
		"concentrationPackageAmount": "",
		"concentrationPackageNotes": "",
		"dose": 1,
		"isApplyPowder": 0,
		"isCapsulePowder": 0,
		"isCream": 0,
		"isCreamGranule": 0,
		"isDecoct": "",
		"isDrychip": 0,
		"isExtract": 0,
		"isExtractGranule": 0,
		"isFeetPowder": 0,
		"isMaskPowder": 0,
		"isSachetPowder": 0,
		"isSwallowPowder": 0,
		"isTeaPowder": 0,
		"isPillowPowder": 0,
		"packType": "",
		"pillType": "",
		"takeDays": 1,
		"timesPerDay": 3,
		"usageMode": "",
		"powderPackageAmountTip": "",
		"packageTypeName": ""
	},
	"doctAdvice": {
		"notesDoctor": "",
		"others": "",
		"taboo": "",
		"usageBrief": "",
		"usageMethod": "每天3次,每次1颗",
		"usageTime": "饭后半小时"
	},
	"from": 0
}
	r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
	print(r.json())
	return r.json()['data']

def create_shuiwan():
	url = "https://test.igancao.cn:8000/gateway/treatment/cloudRecipel/creatCloudRecipel"
	headers = login.headers
	data = {
	"sort": 8,
	"prescriptionId": 2782,
	"dfId": 106,
	"dsId": 1,
	"medicineList": [{
		"id": 269,
		"quantity": 1000,
		"brief": ""
	}],
	"ctmExt": {
		"amount": 1,
		"bolusSpec": "",
		"concentrationPackageAmount": "",
		"concentrationPackageNotes": "",
		"dose": 5,
		"isApplyPowder": 0,
		"isCapsulePowder": 0,
		"isCream": 0,
		"isCreamGranule": 0,
		"isDecoct": "",
		"isDrychip": 0,
		"isExtract": 0,
		"isExtractGranule": 0,
		"isFeetPowder": 0,
		"isMaskPowder": 0,
		"isSachetPowder": 0,
		"isSwallowPowder": 0,
		"isTeaPowder": 0,
		"isPillowPowder": 0,
		"packType": "",
		"pillType": "",
		"takeDays": 50,
		"timesPerDay": 3,
		"usageMode": "",
		"powderPackageAmountTip": "",
		"packageTypeName": ""
	},
	"doctAdvice": {
		"notesDoctor": "",
		"others": "",
		"taboo": "",
		"usageBrief": "",
		"usageMethod": "一天3次，一次5g",
		"usageTime": "饭后半小时"
	},
	"from": 0
}
	r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
	print(r.json())
	return r.json()['data']

def create_shuimiwan():
	url = "https://test.igancao.cn:8000/gateway/treatment/cloudRecipel/creatCloudRecipel"
	headers = login.headers
	data = {
	"sort": 9,
	"prescriptionId": 2782,
	"dfId": 107,
	"dsId": 2,
	"medicineList": [{
		"id": 750,
		"quantity": 1000,
		"brief": ""
	}],
	"ctmExt": {
		"amount": 1,
		"bolusSpec": "",
		"concentrationPackageAmount": "",
		"concentrationPackageNotes": "",
		"dose": 5,
		"isApplyPowder": 0,
		"isCapsulePowder": 0,
		"isCream": 0,
		"isCreamGranule": 0,
		"isDecoct": "",
		"isDrychip": 0,
		"isExtract": 0,
		"isExtractGranule": 0,
		"isFeetPowder": 0,
		"isMaskPowder": 0,
		"isSachetPowder": 0,
		"isSwallowPowder": 0,
		"isTeaPowder": 0,
		"isPillowPowder": 0,
		"packType": "",
		"pillType": "",
		"takeDays": 56,
		"timesPerDay": 3,
		"usageMode": "",
		"powderPackageAmountTip": "",
		"packageTypeName": ""
	},
	"doctAdvice": {
		"notesDoctor": "",
		"others": "",
		"taboo": "",
		"usageBrief": "",
		"usageMethod": "一天3次，一次5g",
		"usageTime": "饭后半小时"
	},
	"from": 0
}
	r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
	print(r.json())
	return r.json()['data']

def create_zhongchengyao():
	url = "https://test.igancao.cn:8000/gateway/treatment/cloudRecipel/creatCloudRecipel"
	headers = login.headers
	data = {
	"sort": 10,
	"prescriptionId": 2782,
	"dfId": 118,
	"dsId": 5,
	"medicineList": [{
		"id": 4460,
		"quantity": 1,
		"brief": "外用，1-2次/周，适量"
	}],
	"ctmExt": {
		"amount": "",
		"bolusSpec": "",
		"concentrationPackageAmount": "",
		"concentrationPackageNotes": "",
		"dose": 1,
		"isApplyPowder": 0,
		"isCapsulePowder": 0,
		"isCream": 0,
		"isCreamGranule": 0,
		"isDecoct": "",
		"isDrychip": 0,
		"isExtract": 0,
		"isExtractGranule": 0,
		"isFeetPowder": 0,
		"isMaskPowder": 0,
		"isSachetPowder": 0,
		"isSwallowPowder": 0,
		"isTeaPowder": 0,
		"isPillowPowder": 0,
		"packType": "",
		"pillType": "",
		"takeDays": 1,
		"usageMode": "",
		"packageTypeName": ""
	},
	"doctAdvice": {
		"notesDoctor": "",
		"others": "",
		"taboo": "",
		"usageBrief": "",
		"usageMethod": "",
		"usageTime": ""
	},
	"from": 0
}
	r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
	print(r.json())
	return r.json()['data']

def create_putonggaofang():
	url = "https://test.igancao.cn:8000/gateway/treatment/cloudRecipel/creatCloudRecipel"
	headers = login.headers
	data =  {
	"sort": 11,
	"prescriptionId": 2782,
	"dfId": 130,
	"dsId": 1,
	"medicineList": [{
		"id": 270,
		"quantity": 1000,
		"brief": ""
	}],
	"ctmExt": {
		"amount": "",
		"bolusSpec": "",
		"concentrationPackageAmount": "30-40包",
		"concentrationPackageNotes": "浓度较稀",
		"dose": 1,
		"isApplyPowder": 0,
		"isCapsulePowder": 0,
		"isCream": 0,
		"isCreamGranule": 0,
		"isDecoct": "",
		"isDrychip": 0,
		"isExtract": 1,
		"isExtractGranule": 0,
		"isFeetPowder": 0,
		"isMaskPowder": 0,
		"isSachetPowder": 0,
		"isSwallowPowder": 0,
		"isTeaPowder": 0,
		"isPillowPowder": 0,
		"packType": "",
		"pillType": "",
		"takeDays": 1,
		"usageMode": "",
		"powderPackageAmountTip": "",
		"packageTypeName": "饮片流浸膏小包装"
	},
	"doctAdvice": {
		"notesDoctor": "",
		"others": "",
		"taboo": "",
		"usageBrief": "",
		"usageMethod": "",
		"usageTime": ""
	},
	"from": 0
}
	r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
	print(r.json())
	return r.json()['data']

def create_kelijigaofang():
	url = "https://test.igancao.cn:8000/gateway/treatment/cloudRecipel/creatCloudRecipel"
	headers = login.headers
	data = {
	"sort": 12,
	"prescriptionId": 2782,
	"dfId": 140,
	"dsId": 3,
	"medicineList": [{
		"id": 296,
		"quantity": 5000,
		"brief": ""
	}],
	"ctmExt": {
		"amount": "",
		"bolusSpec": "",
		"concentrationPackageAmount": "30-40包",
		"concentrationPackageNotes": "",
		"dose": 1,
		"isApplyPowder": 0,
		"isCapsulePowder": 0,
		"isCream": 0,
		"isCreamGranule": 0,
		"isDecoct": "",
		"isDrychip": 0,
		"isExtract": 0,
		"isExtractGranule": 1,
		"isFeetPowder": 0,
		"isMaskPowder": 0,
		"isSachetPowder": 0,
		"isSwallowPowder": 0,
		"isTeaPowder": 0,
		"isPillowPowder": 0,
		"packType": "",
		"pillType": "",
		"takeDays": 1,
		"usageMode": "",
		"powderPackageAmountTip": "",
		"packageTypeName": "颗粒剂流浸膏小包装"
	},
	"doctAdvice": {
		"notesDoctor": "",
		"others": "",
		"taboo": "",
		"usageBrief": "",
		"usageMethod": "",
		"usageTime": ""
	},
	"from": 0
}
	r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
	print(r.json())
	return r.json()['data']



