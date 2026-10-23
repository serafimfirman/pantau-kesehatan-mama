import ctypes, sys, wave, espeakng_loader as E
lib = ctypes.CDLL(E.get_library_path())
CB = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_short), ctypes.c_int, ctypes.c_void_p)
buf = bytearray()
def cb(wav, n, ev):
    if wav and n > 0: buf.extend(ctypes.string_at(wav, n * 2))
    return 0
cbf = CB(cb)
rate = lib.espeak_Initialize(2, 500, E.get_data_path().encode(), 0)
lib.espeak_SetSynthCallback(cbf)
voice, text, out = sys.argv[1], sys.argv[2], sys.argv[3]
speed = int(sys.argv[4]) if len(sys.argv) > 4 else 150
pitch = int(sys.argv[5]) if len(sys.argv) > 5 else 50
lib.espeak_SetVoiceByName(voice.encode())
lib.espeak_SetParameter(1, speed, 0)  # rate
lib.espeak_SetParameter(3, pitch, 0)  # pitch
lib.espeak_SetParameter(4, 30, 0)     # range
t = text.encode('utf-8')
lib.espeak_Synth(t, len(t) + 1, 0, 0, 0, 0x01, None, None)  # espeakCHARS_UTF8
lib.espeak_Synchronize()
with wave.open(out, 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(bytes(buf))
print(out, len(buf)/2/rate, 's')
