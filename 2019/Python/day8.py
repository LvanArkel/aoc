def load_layers(w, h, data):
    return [data[i:i + w * h] for i in range(0, len(data), w * h)];


def lowest_layers(layers):
    least_layer = None
    least_count = 25*6+1
    for layer in layers:
        count = count_numbers(layer, '0')
        if count < least_count:
            least_layer = layer
            least_count = count
    return least_layer, least_count

def count_numbers(layer, digit):
    count = 0
    for dig in layer:
        if digit == dig:
            count += 1
    return count

def decode_layers(w, h, layers):
    result = [-1]*(w*h)
    for i in range(w*h):
        for j in range(len(layers)):
            if layers[j][i] == '1':
                result[i] = '■'
                break
            elif layers[j][i] == '0':
                result[i] = ' '
                break
    return result

def print_image(w, h, layer):
    for i in range(0, w*h, w):
        print(layer[i:i+w])

def show_image(w,h,data):
    print_image(w,h,decode_layers(w,h,load_layers(w,h,data)))

testdata = "123456789012"
testdata2 = "02221122221200000"

print("Test Q1")
print(load_layers(3, 2, testdata))
print("Test Q2")
show_image(2,2,testdata2)


with open("input/day8.txt") as f:
    contents = f.read()
    layers = load_layers(25, 6, contents)
    print("Q1")
    lowest_layer = lowest_layers(layers)
    print(lowest_layer)
    print(count_numbers(lowest_layer[0], '1')*count_numbers(lowest_layer[0], '2'))
    print("Q2")
    show_image(25,6,contents)
