import requests
import sys
import os
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def request_waf(ip_list, rule_name, domain):
    burp0_url = "https://yundun.console.aliyun.com:443/openapi/waf-openapi/2019-09-10/CreateProtectionModuleRule.json"
    burp0_cookies = {
    your_cookies
    }
    burp0_headers = {
    your_headers
    }
    ip_str = ",".join(ip_list)
    rule = {
        "action": "block",
        "name": rule_name,
        "scene": "custom_acl",
        "conditions": [{
            "opCode": 1,
            "key": "IP",
            "values": ip_str
        }]
    }
    data_dict = {
        "Region": "cn",
        "InstanceId": your_InstanceId,  //请求包中找“实例ID”
        "Domain": domain,
        "Rule": rule,
        "DefenseType": "ac_custom"
    }
    burp0_data = {
        "regionId": your_regionId,
        "data": json.dumps(data_dict, ensure_ascii=False),  //这一句不要改
        "secToken": your_secToken,
        "token": your_token,
        "collina": "your_collina"
    }
    response = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data, verify=False)
    print(f"Rule name: {rule_name}, Status: {response.status_code}, Response: {response.text}")
    return response.status_code

def main(txt_path, name_prefix, name_start):
    if not os.path.isfile(txt_path):
        print("文件不存在")
        return
    with open(txt_path, "r") as f:
        ips = [line.strip() for line in f if line.strip()]
    group_size = 50
    domains = [
        "your_domain1",
        "your_domain2",
    ]
    for domain in domains:
        for idx, i in enumerate(range(0, len(ips), group_size)):
            ip_group = ips[i:i+group_size]
            rule_name = f"{name_prefix}{name_start+idx}"
            request_waf(ip_group, rule_name, domain)


if __name__ == "__main__":

    txt_path = "your_ip_list_file_path"   //指定需要封禁ip的txt文件位置
    name_prefix = "your_rule_name_prefix"   //规则名前缀，例如：202507014_
    # int
    name_start = your_rule_name_prefix   //序号（整数型），和前缀拼接，例如值为1时，生成：202507014_1、202507014_2、202507014_3
    main(txt_path, name_prefix, name_start)

