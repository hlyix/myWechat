import json
import urllib.request

def f(user,txt):
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    req = {
        "perception":
        {
            "inputText":
            {
                "text": txt
            },

            "selfInfo":
            {
                "location":
                {
                    "city": "长沙",
                    "province": "湖南",
                    "street": "麓山南路"
                }
            }
        },

        "userInfo":
        {
            "apiKey": "411ff4c888134fd8bfe3aa2b9302834e",
            "userId": user
        }
    }
    # print(req)
    # 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
    # print(req)

    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    # print(response_str)
    response_dic = json.loads(response_str)
    # print(response_dic)

    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    print('code：' + str(intent_code))
    print('text：' + results_text)
    return results_text

def test():
    while(True):
        f("haluo",input());

# test()