from web3 import Web3
import json
import time

while True:
    time.sleep(2)
    try:
        print("IN")
        w3 = Web3(Web3.HTTPProvider("https://cloudflare-eth.com/")) 
        with open('./ABI.json') as f:
            ABI = json.load(f)
            f.close()
            HFC = w3.eth.contract(address=Web3.toChecksumAddress('0xe1b2ba089ea5ac932dad7d98b897a895d681d3a6'),abi=ABI)
            while True:
                time.sleep(0.5)
                pricee = (HFC.functions.price().call()/(10**18))
                totalsupply = (HFC.functions.totalSupply().call()/(10**18))
                with open('./DATA.json','r') as k:
                    data = (json.load(k))
                    if (list(data["ETH"]["PRICE"].values())[-1]) != pricee:
                        data["ETH"]["PRICE"][str(int(time.time()))] = pricee
                        k.close()
                        with open('./DATA.json','w') as l:
                            l.write("")
                            l.write(json.dumps(data))
                            print(data)
                            l.close()
                    else:
                        k.close() 
                with open('./DATA.json','r') as m:
                    data = (json.load(m))
                    if (list(data["ETH"]["TOTALSUPPLY"].values())[-1]) != totalsupply:
                        data["ETH"]["TOTALSUPPLY"][str(int(time.time()))] = totalsupply
                        m.close()
                        with open('./DATA.json','w') as n:
                            n.write("")
                            n.write(json.dumps(data))
                            print(data)
                            n.close()
                    else:
                        m.close()
    except Exception as e:
        print("Error:",e)
