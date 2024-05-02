def q1(number):
    
    if number <=1:
        return []

    factors = []
    primes = [2]

    for prime_num in primes:
        if prime_num**2 > number:
            if number > 1:
                factors.append((number, 1))
            break

        count_p = 0
        while number % prime_num == 0:
            number = number // prime_num
            count_p +=1

        if count_p != 0:
            factors.append((prime_num, count_p))

        #add the next prime number to 'primes' list
        next_prime_num = prime_num+1
        loop = True
        while loop:
            for prime in primes:
                if next_prime_num % prime == 0:
                    if prime == 2:
                        next_prime_num += 1
                    else :
                        next_prime_num += 2
                    break
                
                if prime**2 > next_prime_num:
                    primes.append(next_prime_num)
                    loop = False
                    break
    return factors
