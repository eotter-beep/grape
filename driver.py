from audio2vec import Audio2Vec
import quantumaudio
import numpy
import anyio

# Create a memory object stream
send_stream, receive_stream = anyio.create_memory_object_stream(10)

# Example usage inside async context
async def use_streams():
    async with send_stream, receive_stream:
        await send_stream.send("hello")
        item = await receive_stream.receive()
        print("Received:", item)

audsend = send_stream
processor = Audio2Vec(audsend)
# We need a asarray feature of dimensions
dimensions = numpy.asarray(30332)
feature = Audio2Vec(nFeatures=dimensions)
# Load the QPam scheme
qpam = quantumaudio.load_scheme("qpam") # or directly access from quantumaudio.schemes.QPAM()
# Define an Input
original_data = quantumaudio.tools.test_signal() # for a random array of samples (range: -1.0 to 1.0)

# Encoding
encoded_circuit = qpam.encode(original_data)

# Decoding
decoded_data  = qpam.decode(encoded_circuit,shots=4000)