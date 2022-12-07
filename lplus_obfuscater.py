from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import zlib
import hashlib

#https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/

def encryption(item):
    """
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    """
    print(item)

    if isinstance(item,int):
        item=str(item)

    if isinstance(item,type(None)) or item=="None" or item=="":
        return item
    elif isinstance(item,str):
        item_bytes=bytes(item, 'utf-8')

    """
    item_to_encrypt = item_bytes
    
    
    item_encrypted = public_key.encrypt(
        item_to_encrypt,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    """
    item_encrypted = hashlib.sha256(item_bytes).hexdigest()

    return item_encrypted

def obfuscate(rest_response):
    data_points_to_obfuscate=["pId1","userName","password","firstName","lastName","dateOfBirth","gender","salutation","title","nativeFirstName","nativeLastName","isoCountryOfBirth","dateOfBirth","cityOfBirth","email","street","zipCode","city","isoCountry"]
    rest_response=rest_response
    if isinstance(rest_response,dict):
        rest_response=[rest_response]
    if isinstance(rest_response,list):
        json_response=rest_response

        for eintrag in json_response:
            def traversing_nested_lists(json_response):
                nested_dict=json_response
                print(nested_dict)
                if isinstance(nested_dict,dict):
                    for key,item in nested_dict.items():
                        print(f"Iteriere über {key,item}")
                        if isinstance(item,list):
                            print(f"Rekursion bei: {key}")
                            traversing_nested_lists(item[0])
                        else:
                            if key in data_points_to_obfuscate:
                                item_encrypted=encryption(item)
                                nested_dict[key]=item_encrypted
                                print(f"Ersetze hier: {key,item}")
        
            traversing_nested_lists(eintrag)

    print(rest_response)
    return rest_response

#rest_response=lplus_request(access_token)
#obfuscated_response=obfuscate(rest_response)

def decryption():
    obfuscated_response=[{"test":b"o\xfe~i\xd2\xeb\x0f\xc3\xf0\xf7\xb6\xee_k4,\xe9\x83\xa9\xa0\x867\xd6\xee\xf4\x9d\xbd\x81\n\xd8}ln\xd7\xd3\xc1r\x9b.\xa4\xbe$\xac!D\xa4\xe8\xbc \x9a\x00\xffG2\x8b\xe01Xg\xe2|\x18\xdd\xa2\x10\x07jt\x94I\x00\xc7x\xa5w\xef\xf0\t\xb2\x84\xc7\xd6U\x9a\xc2A\n[\xc6r\xdau\x17\xae\x8bN4\x10\xc6\x81]\xc1&\xf8\x17\xe0>T\xe2\xfaxo\xe3\x9e\xf9\xa3S&\x19\x14\x92@0\x92\xf6)\xed\xbe\xef\x99\x9e\xe4\xe0\x90\xf8>D\x93O\xca\n\x90\x86v\x0c\xf1\xf3\xb6\xa5\xe9\xaf\xee\xa2\xb6\xc4\x14Fk\xa3Eb\x91<}[\xbd6\xd6\x93\xd5\x1c\x8a\x16s\x00\xce\xf4\x84$\x19\x9e\xecX\xcd\x94\xaa-\xe1\x97\xfe\x8c\x95\xdbJ\x11U\xf1\xd9<p\xc74\xb8\x1b\xa0\x8d\xdb\xf6\xcd\xf9\xba\xc1\xcd\xa8\x9eW\xc0\xdfU1:\xee,\xea%\x93\x00\x93Y\x8b\xbf\xc3\xc2\x9cc^\xd7\x1dph\xd0h\xa2\x96\x93$\xccE\xdbH\xca\xb1(}F*"}]
    for key,item in obfuscated_response[0].items():
        if isinstance(item,bytes):
            with open("private_key.pem", "rb") as key_file:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                    backend=default_backend()
        )
            original_message = private_key.decrypt(
            item,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
            )
            print(key, item, original_message,"\n")
