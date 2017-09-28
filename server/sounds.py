from flask import jsonify
import re
import os
from random import Random
import socket
from player import Player


activePlayers = {}
SERVER_ADDRESS = 'http://%s:5000/static/sounds/'
INSTRUMENTS = [ 
    'bass',
    'guitar',
    'piano',
    'all' ]

EASY = 'easy'
HARD = 'hard'


bassArray = []
guitarArray = []
pianoArray = []
currentArray = []

def getKeyNote(playerID, mode, instrument, keyParam):
    if instrument == INSTRUMENTS[0]:
        currentArray = bassArray
    elif instrument == INSTRUMENTS[1]:
        currentArray = guitarArray
    elif instrument == INSTRUMENTS[2]:
        currentArray = pianoArray
    else:
        random = Random()
        randInstrument = random.randint(0, 3)
        return getKeyNote(mode, INSTRUMENTS[randInstrument], keyParam)
    
    # Gets a random position of array
    random = Random()
    pos = random.randint(0, len(currentArray) - 1)
    dictKeyNote = currentArray[pos]
    # Gets the key and the value of dictionary 
    key = "%s.mp3" % dictKeyNote.keys()[0] # Ex: oPvGpkBLFZgkzKtUxxoQohFJYorKjEKY
    value = dictKeyNote[dictKeyNote.keys()[0]] # Ex: a0

    # Call getKeyNote if is easy mode and the key getted is sharp
    if mode == EASY and isSharpKey(value):
        return getKeyNote(playerID, mode, instrument, keyParam)

    pathKey = getKeyPathAsJson(instrument, key)
    activePlayer = activePlayers[playerID]
    # saving current key and value to be compared later
    activePlayer.setCurrentKey(dictKeyNote)
    return pathKey

def getKeyPathAsJson(instrument, key):
    global currentInstrument
    pathKey = SERVER_ADDRESS + instrument + '/' + key
    return jsonify(address = pathKey)

def isSharpKey(key):
    regex = re.compile(r's')
    return regex.search(key);

def match(playerID, userKey):
    activePlayer = activePlayers[playerID]
    playerKeyNote =  activePlayer.getCurrentKey()
    if playerKeyNote is None:
        return activePlayer.toJSON()
    
    key = playerKeyNote.keys()[0]
    value = playerKeyNote[key]
    value = re.sub(r'\d+', '', value)
    if value == userKey.lower():
        activePlayer.updateScore()
    activePlayer.setCurrentKey(None)
    return activePlayer.toJSON()

def resetData(playerID):
    global SERVER_ADDRESS
    host = socket.gethostbyname(socket.getfqdn())
    SERVER_ADDRESS = 'http://%s:5000/static/sounds/' % (host)
    bassArray = []
    guitarArray = []
    pianoArray = []
    currentArray = []
    playerInstance = Player(playerID)
    activePlayers[playerID] = playerInstance
    # playerInstance.resetScore() //TODO is it really necessary?
    loadKeyNotes()
    return activePlayers[playerID].toJSON();

def loadKeyNotes():
    bassArray.append({'UsooaSPxhZhkYgNicYdcgahIRwveRYuD': 'a0.mp3'})
    bassArray.append({'WxQmchAtCpqAMlIpSpDcbJeILzeTpwjC': 'a1.mp3'})
    bassArray.append({'default': 'a2.mp3'})
    # bassArray.append({'SLIrNGhENQffmhsjBuVIgxhPMhsxXvXo': 'a2.mp3'})
    bassArray.append({'oPMlOgOXIcLQWeDBpwTIpuvYbRxrkluf': 'as.mp3'})
    bassArray.append({'bMDCZAODoAELqRPuCaUGsZmDNTCKxFyB': 'as1.mp3'})
    bassArray.append({'QWuwMtQpvcsebtqwQxZFyOkoszAdXkex': 'as2.mp3'})
    bassArray.append({'aCvkzGaNhATOorVimIRhHRqOsijeANjR': 'b0.mp3'})
    bassArray.append({'hdAlvycqeOzKkUDEpfskGSVmnkEZmrsd': 'b1.mp3'})
    bassArray.append({'eHMJBZFVkvosBXYURFRWGtSjepfQfcMK': 'b2.mp3'})
    bassArray.append({'btMtBlpgaWzFFKfQjLlgZeIjNPMpTmIC': 'c0.mp3'})
    bassArray.append({'nwNtmVVbiNSlmmgjvldKUpEmoupADuET': 'c1.mp3'})
    bassArray.append({'QVcaTCDNGmscOgtaGQbDIrsVIEansJkX': 'c2.mp3'})
    bassArray.append({'MdVGvNdpMNVNIJzzladQuPKyDlnIUzmj': 'c28.mp3'})
    bassArray.append({'XdScLHaTerTqkzBJiccwHXQDLCrytTGj': 'cs0.mp3'})
    bassArray.append({'vkMzjrAgttkeKwOzwIZzOcVaHxuAAOVO': 'cs1.mp3'})
    bassArray.append({'WdcIDQtLBzXCmiObDDvBViWSAspWnKiZ': 'cs2.mp3'})
    bassArray.append({'iazTPONzoyQQtwjomWARfpPZNztbLgLD': 'd0.mp3'})
    bassArray.append({'FeFYOblKcJyAFxSqacvTfsrYvmBYnbrT': 'd1.mp3'})
    bassArray.append({'FUrizQIpuMZuHnRPXZgPcLqipaWUusOF': 'd2.mp3'})
    bassArray.append({'hknQQIiMWEMOGvoJOeWxwVbZJtBCiBgI': 'ds.mp3'})
    bassArray.append({'lnFPxMGmnbLLqQAvxgfDbVuqXGLaAdHn': 'ds1.mp3'})
    bassArray.append({'OpwbtfMzxtIholaBjRGXdakYKGlkFyxr': 'ds2.mp3'})
    bassArray.append({'pwMZPZBqiJKySRhJVKuHrZFNvWqAoyez': 'e0.mp3'})
    bassArray.append({'DpkgLGnovVZsDErrVdvzlhXGfDWawjPv': 'e1.mp3'})
    bassArray.append({'DJnFigDjnUZYuMOrmvfcYnupObScjLuz': 'e2.mp3'})
    bassArray.append({'tFCEVynmhjaokDASngHFRmMGzMWsanQZ': 'f0.mp3'})
    bassArray.append({'JgtuCxdVThIChuYYBNrJJSXSzDNSvCLH': 'f1.mp3'})
    bassArray.append({'lklbJyfsSjOeJTqgMOBjxtPMpEazuXuu': 'f2.mp3'})
    bassArray.append({'GQAStVaqFHBYLohwLEvpcVXHnClBduIt': 'fs.mp3'})
    bassArray.append({'CtkqmueFrsbLbCuTJIBoVKDsFAdNbPOg': 'fs1.mp3'})
    bassArray.append({'cJibWKoohufsJeKfaPkRVgTnyQOxCHIc': 'fs2.mp3'})
    bassArray.append({'liKrgyhjOVxmiQcmXTHtabNITrXqOMOy': 'g.mp3'})
    bassArray.append({'xJXVMckAgIAiBEbMHEuiCObLbzHeJtVn': 'g1.mp3'})
    bassArray.append({'KHKYXCGRIzImQorHgpaJmdEkUOyidaGi': 'g2.mp3'})
    bassArray.append({'ksRklszkouVKCRBgYcqKDLfjRIBcXwln': 'gs.mp3'})
    bassArray.append({'tizadoYTpIpzRHHzjxpiYvwsJdbjszsQ': 'gs1.mp3'})
    bassArray.append({'yJUiggvbmaowFarCznuAEVHQytgQsmse': 'gs2.mp3'})

    # bassArray.append({'oPvGpkBLFZgkzKtUxxoQohFJYorKjEKY': 'a0'})
    # bassArray.append({'WNrpilsOoxXibYDFnWUSQRfkqEvAznnn': 'a1'})
    # bassArray.append({'default': 'a2'})
    # # bassArray.append({'nvoOdYAUPFhcVkGApYpPnPNriNiHyrMT': 'a2'})
    # bassArray.append({'YsKyezEjYEvGzXrcdZKZwlsjlpyOBGLd': 'as'})
    # bassArray.append({'JxpbZDIdEPdVxdvGRcpqLALxQlSYlcXR': 'as1'})
    # bassArray.append({'ktZTXSulmwYnqnDKGQqGMzvuROXRepvt': 'as2'})
    # bassArray.append({'fLFwFfBNMrDbJzSHAVdhBeQfumrivWTI': 'b0'})
    # bassArray.append({'bwlDBfQBknEUJhSAzXMMCvEfyWhvYRBZ': 'b1'})
    # bassArray.append({'SFQvOmCQbJiBNTusVMqabLGzQnRKfsMt': 'b2'})
    # bassArray.append({'ITqIEefMcTgLQtMdjNocUJBrXAUhMcOh': 'bkp'})
    # bassArray.append({'xcFGNsqgQPkAhiIHPHPlXXbsrPwrKuPa': 'c0'})
    # bassArray.append({'wLkFMJrDKHqmnorCdHgGBMgmiFZzgPum': 'c1'})
    # bassArray.append({'jfWxSSUfVfWwXNmwZMryDZzjtrbYuMoj': 'c2'})
    # bassArray.append({'rKWIkQZGIHKqzUDePwuBWUaVmWwPmQmG': 'c28'})
    # bassArray.append({'HRYBZvMMDozKoHCKnmFGIPuuMKuesjIy': 'cs0'})
    # bassArray.append({'WYyRMeWofGrxFCatuavghwKWuphYVujN': 'cs1'})
    # bassArray.append({'wBpMhIKJQaVQODtRFSiErXXCCFBaStSI': 'cs2'})
    # bassArray.append({'kmQAeipHhYoKdkgnqSlldUjFEoONAPER': 'd0'})
    # bassArray.append({'KtKSUTRVBiGanqVUgKUphyzZprUHyEEr': 'd1'})
    # bassArray.append({'WJltQYeHLGWREgNMpiXkmCBwvtDzOZwA': 'd2'})
    # bassArray.append({'SIOADyjeiCXLuHkgifnPXqazVDPhyJip': 'ds'})
    # bassArray.append({'fxeWuDCngyGswFYKzgmOfDMjyOvzRJgd': 'ds1'})
    # bassArray.append({'sUdviQdagMXiMCSYzMLrYBeAlmQTVWuH': 'ds2'})
    # bassArray.append({'NshPbmhylnvGZwhOjmAXFbOUBTAquFKH': 'e0'})
    # bassArray.append({'boSQFWrCVODaPuIBmHPvLPxnWfBlaQIS': 'e1'})
    # bassArray.append({'FHEnHHoaVOGcJWvXerWWpinKMxTeOMUy': 'e2'})
    # bassArray.append({'jYMEuMNYFYsNQiMPXIMgivLYToaXyEHU': 'f0'})
    # bassArray.append({'UDOkDkuNJaKHIOZrmQeWaSBvOCnLsnOB': 'f1'})
    # bassArray.append({'ASUKMpPjecLskrrXGLHDlhEcHjStWKFv': 'f2'})
    # bassArray.append({'vfitORlnoyqjoDsfUuGnYdRzbkfGJBIo': 'fs'})
    # bassArray.append({'rQARMKqMBNuwYEGkWXjZyYoIkbHuMqiP': 'fs1'})
    # bassArray.append({'cuuzuABXjZpyBoKBSMggoNIWNBUjVMvT': 'fs2'})
    # bassArray.append({'rNsgFmfiSisoeNSnrUjqKIqwciomxMrp': 'g'})
    # bassArray.append({'EoBikRXxUXwvUDYDOxWcnNaSGmqquAmR': 'g1'})
    # bassArray.append({'LNmEUwhsDuQjqdxpueIidtgfZMrAdXHB': 'g2'})
    # bassArray.append({'TcuCAdaZpTgTJavkjwwzTzwabskRhlTe': 'gs'})
    # bassArray.append({'RTtYrZxFhxtcKeRJCZfYvpYUZQxebLNq': 'gs1'})
    # bassArray.append({'ffgFHwixLEAKpVeZhFKhzRCiMBqDaSaZ': 'gs2'})

    guitarArray.append({'RkwaXJuDKCipdloHPjxHSAWMYkggZrNl': 'a1'})
    guitarArray.append({'default': 'a2'})
    # guitarArray.append({'QNaoYrtYaFYJqfnMMhgrnMGrzzbuojwu': 'a2'})
    guitarArray.append({'hOqhayLCTXiGEmCCMtSBuWkWcwaKIAhn': 'a3'})
    guitarArray.append({'vASFQlDOvDOKMxPNoyabsuSfiLGrqATs': 'a4'})
    guitarArray.append({'wRSjbfJhJVVyyfwwJqFEhYFfHvfWhZEM': 'as1'})
    guitarArray.append({'TBOhAVbpuxUZDeXMydffQAaYJDpYQjgq': 'as2'})
    guitarArray.append({'dHpxWSucHRdDykRYnSDwineTQdBhwIyy': 'as4'})
    guitarArray.append({'weEWYmjHhOTnnTQQfbYKxLCMDgnAIdTD': 'b1'})
    guitarArray.append({'hEZtAtKMPmDSeQlBBlIkIjuQFbBiTKPi': 'b2'})
    guitarArray.append({'WCNXfWbnmKbthBNTONKgquOfLDEYEdtA': 'b4'})
    guitarArray.append({'yNHaHIRPEdDfrcTaConzRvlZfXWaHvdi': 'c'})
    guitarArray.append({'jdNFBPrvIgxtTlCcCOgNTZvUprKEctPg': 'c1'})
    guitarArray.append({'OmkHHlKrQWycSJWFEpEboJIzqIRQEjOM': 'c2'})
    guitarArray.append({'OYlDdohwQzMbbVkCBhSTNsOJxNrqaWIa': 'c3'})
    guitarArray.append({'gaoWPLlJDsAWWUdZspWvpNcJbUVNKzVd': 'cs'})
    guitarArray.append({'HSSfjdgwJgIHaOEVhSTPwHIQNdVWazkA': 'cs1'})
    guitarArray.append({'wdvJlIrmMsvHYRBpPEgBVGahgcKtwMqL': 'cs2'})
    guitarArray.append({'uciPReVgiUgVkyYuoqLwjycnoqCNVhzV': 'cs3'})
    guitarArray.append({'LKhMPmEJXxNQFYQRNkmbZavGwHIzAXam': 'd0'})
    guitarArray.append({'ShhJgRSHPofgNmpetZijGqIliqKnqEVB': 'd1'})
    guitarArray.append({'NIwkogPlIQWknrYgNPMMCwAwZYyfxSam': 'd2'})
    guitarArray.append({'XMyoiGSlYHkduwfclpRMpcpUocsyOneD': 'd3'})
    guitarArray.append({'HPfqJfxeLXxhFlATZChYFbikYTPscunQ': 'ds0'})
    guitarArray.append({'WBGQVLXTPFHYWMGgKwNCRWXRakClkjlH': 'ds1'})
    guitarArray.append({'beRBIvAGLhKlosgOwqwoaduVtCsaOejg': 'ds2'})
    guitarArray.append({'OBouXWQbtBskIEUZHJjzWGZaPulyyzAo': 'ds3'})
    guitarArray.append({'UVtjDLmkVJsASCLFliVunglcRkPOHqlU': 'e0'})
    guitarArray.append({'CxPCggMYnCjKXeCdHAXORfgqjGfPWLbk': 'e1'})
    guitarArray.append({'DuSTHaSfyziQCVEfajqIIdARRoZuXAJP': 'e2'})
    guitarArray.append({'pmWsqhXvoXFiuhxlbDIADTjdsgyLhJuG': 'e3'})
    guitarArray.append({'ovDAkDKAUsRGqkMTBgDyxvzgqiuqyYFv': 'f0'})
    guitarArray.append({'EprPQZYzrlCtFiZXEDvgiwzAQSdpvXwX': 'f1'})
    guitarArray.append({'lvRQxkQVcjtsFzXFpjrqjeNYsgRJahqu': 'f2'})
    guitarArray.append({'JQPyuTTVaVBIEonFOuGgBVwqsSjsdxSP': 'f3'})
    guitarArray.append({'yTnoqlRAoMesLcpBQrzezVBQvpTHZDfG': 'fs0'})
    guitarArray.append({'RpHbXOozepUqVGLLeimxAFRDWdYkkBpR': 'fs1'})
    guitarArray.append({'TvzXquqItvKzVJuxoNdIFndoknqYGVxy': 'fs2'})
    guitarArray.append({'aRRtWqsdwRLWFiFrhQVhzicMQYfRIMYw': 'fs3'})
    guitarArray.append({'KdIyDPpUBMyGHUqUZIzuOZkOREMhFDLh': 'g0'})
    guitarArray.append({'xVYyYPotvrbCyMMMxPktbekOUNogOYVz': 'g1'})
    guitarArray.append({'CgeMrRMuAMNcynpXgoIuWzhaxUXTecTU': 'g2'})
    guitarArray.append({'yQkAasBFEBcVmLdswYOHyCxOyelMHaLf': 'g3'})
    guitarArray.append({'txtnzXKblAZjPQpTYrLLmeOGETCcuShf': 'gs'})
    guitarArray.append({'NRXgHbANftAuOZQtMoXSFOHauNdbDVlE': 'gs1'})
    guitarArray.append({'IMIqCJrnBHWMlPwDXTbvNDFGpfeoemfb': 'gs2'})
    guitarArray.append({'RCHIoSomGrHodyhXhayMWHpWUSlsfeux': 'gs3'})

    pianoArray.append({'hrNxSNowRSSIgdPPSYfxhJRrpPPTmXpF': 'a0'})
    pianoArray.append({'NUNlrdwsNrhCTjpuViUYWvavLASqbhww': 'a1'})
    pianoArray.append({'default': 'a2'})
    # pianoArray.append({'CANqNmRzESaqeUoWWRjTicVtAonnPopl': 'a2'})
    pianoArray.append({'YZSwQHQXacKVidjIqLuwEBarehCHCZvP': 'as0'})
    pianoArray.append({'WTwnbzqIjlZlrQnrdjnUUkOOMYsQpnMa': 'as1'})
    pianoArray.append({'GOmTjguyAtZnGozNnbiITZyQQgHnWKVd': 'as2'})
    pianoArray.append({'RHiIqIKZLPoEjOPMTECEyJfcTZpHgwRi': 'b0'})
    pianoArray.append({'WOAtyNncORkgNPjxRqFNaXNfNUkNgeHC': 'b1'})
    pianoArray.append({'IhTQvGquVJfXPuVmfBFAPjwRTrasJUSp': 'b2'})
    pianoArray.append({'TQSKjWeRhWpJEWaWacvvuzEBmZGSDqbq': 'c0'})
    pianoArray.append({'iyoRxMDePsKxgAJgbRtWUcclNhgpXBOs': 'c1'})
    pianoArray.append({'GxRlnkFQVseWxhVIseBBXVVHzDNEPHic': 'c2'})
    pianoArray.append({'SYqgwAAtqidblxwuGyRusHVkwpkDggUm': 'cs0'})
    pianoArray.append({'WYkFwtdVWvERVoseiEHGfCVIhxDHafpo': 'cs1'})
    pianoArray.append({'wgujKHvkGMGlLoidiroTeziYPZEqvysK': 'cs2'})
    pianoArray.append({'oguKuGHNfPayHRrCXmjwlgDFnrWbNPOl': 'd0'})
    pianoArray.append({'RohYBWCJoxzhRjnjzCivtCFPmTHMqulv': 'd1'})
    pianoArray.append({'itbPClFPLvxOintdOGugQCJUpleHRVna': 'd2'})
    pianoArray.append({'BdwoAKvShzXeNWoeHpHZJwIhRZhiRofB': 'ds0'})
    pianoArray.append({'atQXNaLUKjUqUewXIQtXXwneDItwsbqx': 'ds1'})
    pianoArray.append({'EhxZSvQvSeUvJLyHIdtXeLgfyJihuoRK': 'ds2'})
    pianoArray.append({'mGuylQbowXPEzaDkrHhJHZxJRlzbtyct': 'e0'})
    pianoArray.append({'kQrXVqyXtZDaQtiifMJzzkqIrSQffneF': 'e1'})
    pianoArray.append({'KbOeFpYjXExMqsOBvYHDngELKfQDBnEk': 'e2'})
    pianoArray.append({'tMqyPzAAOXEPOqdPEdByYDgexNcPRhkz': 'f0'})
    pianoArray.append({'rhXWxsGFbdvEEPguuFmhzgYWLSgmkKpz': 'f1'})
    pianoArray.append({'uxOCGPyEtpwDmhvoGwpywQxFkgeMHZgq': 'f2'})
    pianoArray.append({'GIFEBfwDlfYdnsOlxJOoeijwkRRrBRgK': 'fs'})
    pianoArray.append({'FvuIyVErtNDOxWsLwnDREUcrCReRIJDP': 'fs1'})
    pianoArray.append({'aKAeIANDZfCipLwxYWlebPTjPNrDKWMM': 'fs2'})
    pianoArray.append({'cqVbVLhrySZfwJhZQLWUsJwSBxXrLoeK': 'g0'})
    pianoArray.append({'HUNqXDkGLeSbRHcPWAtdixPhJzdzDMyA': 'g1'})
    pianoArray.append({'KMemLBXEawJhdGBpJqiewqzVCPgnHQuW': 'g2'})
    pianoArray.append({'SmAXNcvJdrBXhkJUqgZPdfgLdAWKTDSE': 'gs0'})
    pianoArray.append({'TzzlvbrfAGYrnYblmLWBbvKkXLtMfdQO': 'gs1'})
    pianoArray.append({'YWKXYxScXbxndEaoXFAKcndimWGBZQaS': 'gs2'})

    
