fn main() {
    let input1 = 13316116;
    let input2 = 13651422;

    let loop1 = findloopsize(input1);
    println!("Loop Size Found: {}", loop1);
    let loop2 = findloopsize(input2);
    println!("Loop Size Found: {}", loop2);
    
    let key1 = transform(loop2, input1);
    let key2 = transform(loop1, input2);

    if key1 == key2 {
        println!("Key pair match, key is: {}", key1);
    } else {
        println!("No key match");
    }
}

fn transform(loops: i64, subj: i64)-> i64 {
    return ((subj % 20201227) * (subj % 20201227)) % 20201227;
}

fn findloopsize(pubkey: i64) -> i64 {
    let mut i = 0;
    let mut t = 0;
    while t != pubkey {
        i += 1;
        t = transform(i, 7);
    }
    return i;
}

/*input = [9033205, 9281649]

def transform(subj, loop):
    val = 1
    for _ in range(loop):
        val *= subj
        val = val % 20201227
    return val

# Given result, need to find loop size

def findloopsize(public):
    i = 0
    while True:
        t = transform(7, i)
        #print(i, t)
        if t == public:
            return i
        i += 1

def findloopsizeadv(public):
    #public = transform(7, x)
    public = val % 20201227

loop1 = findloopsize(input[0])
loop2 = findloopsize(input[1])
print(loop1, loop2)


result1 = transform(input[0], loop2)
result2 = transform(input[1], loop1)

if result1 == result2:
    print("Succesfully found, key:", result1)
*/