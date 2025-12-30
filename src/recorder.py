import pynput, time, struct

buffer = bytearray()

start = time.perf_counter_ns()

#EVENT TIMESTAMP, EVENT TYPE, EVENT PAYLOAD
#UINT64, UINT8, UINT16
EVENT_FMT = "<QBH"

#EVENT TYPES:
#KEY_DOWN = 0
#KEY_UP = 1

def captured_key_press(key:pynput.keyboard.Key|pynput.keyboard.KeyCode):
	tmp=0
	if isinstance(key,pynput.keyboard.KeyCode):
		tmp=key.vk
	elif isinstance(key,pynput.keyboard.Key):
		tmp=key.value.vk
	buffer.extend(struct.pack(EVENT_FMT,time.perf_counter_ns()-start,0,tmp))
def captured_key_release(key:pynput.keyboard.Key|pynput.keyboard.KeyCode):
	tmp=0
	if isinstance(key,pynput.keyboard.KeyCode):
		tmp=key.vk
	elif isinstance(key,pynput.keyboard.Key):
		tmp=key.value.vk
	buffer.extend(struct.pack(EVENT_FMT,time.perf_counter_ns()-start,1,tmp))

kb_listener = pynput.keyboard.Listener(on_press=captured_key_press,on_release=captured_key_release)

kb_listener.start()
time.sleep(10)
kb_listener.stop()

#chatgpt written for-loop that just prints the data in the bytearray in a human readable way
for i in range(0, len(buffer), struct.calcsize(EVENT_FMT)):
    chunk = buffer[i:i+struct.calcsize(EVENT_FMT)]
    dt_ns, event_type, key_code = struct.unpack(EVENT_FMT, chunk)
    print(f"{dt_ns} {event_type} {key_code}")