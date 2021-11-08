import  socket
from sys import getsizeof
from CompressAndDecompress import Compressed
from EncrytAndDecrypt import  Encrypt

class Client:
    def __init__(self,client_sms,key):
        self.target_host ='localhost'
        self.target_port = 9999
        self.ClientMessage =bytes(client_sms,'utf-8')
        self.key = bytes(key,'utf-8')
        self.iden = bytes(',','utf-8')

    def runClient(self):
        client=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        client.connect((self.target_host,self.target_port))

        print(f'Type of sms{type(self.ClientMessage)}: Type of key{type(self.key)}')
        smsAndKey = self.ClientMessage + self.iden + self.key
        client.send(smsAndKey)

        recvFromServer=client.recv(4096)
        print(f'Back received from server: {recvFromServer.decode("utf-8")}')

        #ToEncryptDataFromServer
        testString = recvFromServer.decode("utf-8")
        testString = testString.split(',')
        print("TestString",testString)
        # print(f'From Server  CypherText{testString[0]} : Key:{testString[1]}')
        cypherText: int = int(testString[0])
        cypherKey: int = int(testString[1])

        toEcrypt = Encrypt()
        DecryptedData: int = int(toEcrypt.decrypt(cypherText, cypherKey))

        print("Decrypted Data:", DecryptedData)
        # print("Decrypted Data: Type", type(DecryptedData))

        #To Decompress Here
        deCompressed:Compressed = Compressed()
        DecompressedDataFromServer = deCompressed.decompress(DecryptedData)
        print("From Server ",DecompressedDataFromServer)

        client.close()

if __name__=="__main__":
    while True:
        Clientsms = input("Enter data to send>:")
        print("Original Data Size is:> {0} bytes".format(getsizeof(Clientsms)))

        Compress: Compressed=Compressed()
        CompressedDatainBin=Compress.compress(Clientsms)
        print("Compressed Size {0} Bytes".format(getsizeof(CompressedDatainBin)))

        # print("Compress.bit_string:>",type(Compress.bit_string)) #int type

        #change int to string
        clientSMS:str = str(CompressedDatainBin)
        objEncrypt=Encrypt()
        CypherText,Key = objEncrypt.encrypt(clientSMS)

        print("CyphterText is:::::: and Key ",CypherText ,Key)

        # tcpClient=Client(clientSMS)
        # tcpClient.runClient()
        print("type of cypherTExt",type(CypherText))

        tcpClient = Client(str(CypherText),str(Key))
        tcpClient.runClient()
