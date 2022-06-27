from web3 import Web3
import json
import time

while True:
    time.sleep(2)
    try:
        print("IN")
        w3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com")) 
        with open('./ABIM.json') as f:
            ABI = json.load(f)
            f.close()
            HFC = w3.eth.contract(address=Web3.toChecksumAddress('0x71c7dC9fb778BE284085Eb5c68cb29B72A88E236'),abi=ABI)
            while True:
                time.sleep(0.5)
                pricee = (HFC.functions.price().call()/(10**18))
                totalsupply = (HFC.functions.totalSupply().call()/(10**18))
                with open('./DATA.json','r') as k:
                    data = (json.load(k))
                    if (list(data["MATIC"]["PRICE"].values())[-1]) != pricee:
                        data["MATIC"]["PRICE"][str(int(time.time()))] = pricee
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
                    if (list(data["MATIC"]["TOTALSUPPLY"].values())[-1]) != totalsupply:
                        data["MATIC"]["TOTALSUPPLY"][str(int(time.time()))] = totalsupply
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
