from web3 import Web3
import json
import time

while True:
    try:
        time.sleep(1)
        w3BSC = Web3(Web3.HTTPProvider("https://speedy-nodes-nyc.moralis.io/db66f798f03c28b4ccf9b81c/bsc/mainnet")) 
        with open('./ABI.json') as f:
            ABI = json.load(f)
            f.close()
            HFCBSC = w3BSC.eth.contract(address='0x849741B79bc1618b46CF9ec600E94E771DEde601',abi=ABI)
            while True:
                time.sleep(2)
                for i in range(1,50):
                    pricee = (HFCBSC.functions.price().call()/(10**18))
                    totalsupply = (HFCBSC.functions.totalSupply().call()/(10**18))
                    with open('./DATA.json','r') as k:
                        data = (json.load(k))
                        if (list(data["BSC"]["PRICE"].values())[-1]) != pricee:
                            data["BSC"]["PRICE"][str(int(time.time()))] = pricee
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
                        if (list(data["BSC"]["TOTALSUPPLY"].values())[-1]) != totalsupply:
                            data["BSC"]["TOTALSUPPLY"][str(int(time.time()))] = totalsupply
                            m.close()
                            with open('./DATA.json','w') as n:
                                n.write("")
                                n.write(json.dumps(data))
                                print(data)
                                n.close()
                        else:
                            m.close()
    except:
        print("Error")
