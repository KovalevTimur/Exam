def read_code(filename):
    code = dict()
    reverse_code = dict()

    # TODO
    file1=open(filename)
    lines=file1.readlines()
    for line in lines:
        tokens=line.split()
    return code, reverse_code

def read_message(filename):
    message = ''

    # TODO
    file1=open(filename)
    message=file1.readlines()

def decoder(encoded_message, reverse_code):
    decoded_message = ''

    # TODO
    return decoded_message

def encoder(message, code):
    encoded_message = ''

    # TODO
    for line in message:
        with open("message.txt", "r", encoding=message) as file:
            text = file.read()
        print(message.rjust(12), "|", text)

    return encoded_message

### PROGRAM GOES HERE ###

# Read code file
code, reverse_code = read_code('code.txt')
 
# Read message file
message = read_message('message.txt')
print("Original  (encoded) message:", message)
 
# Decode message
decoded_message = decoder(message, reverse_code)
print("Decoded message:", decoded_message)

# Encode message
encoded_message = encoder(decoded_message, code)
print("Encoded message", encoded_message)
