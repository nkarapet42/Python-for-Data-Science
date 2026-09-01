ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list.append("World!")
ft_tuple = (ft_tuple[0], "Armenia!")
ft_set.remove("tutu!")
ft_set.add("Yerevan!")
ft_dict["Hello"] = "42Yerevan!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)