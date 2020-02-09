temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26)] .  #data x

c_to_f = lambda data: (data[0], (9.0/5) * data[1] + 32) .       #function f(x)

ftempts = list(map(c_to_f, temps)) .      #Map function

print(ftempts)


"""
  Explain:
        map(x, f(x)) or map(f(x), x) function has 2 variable x and f(x):
          x is the data.
          f(x) is the function.
        
        Map function will take the data x and process f(x) function 
         
"""
