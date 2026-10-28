import random

a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,;/!%éàèêîôöïë()[]=+-@&1234567890*$_<>|~'.?"
b="Hride4xSB UyVg._IöTZbvp@Fé5D78nP~,=jJ6RNo!lè'm[K?tX+O*$|qGWaêzQMôEYsîL-ï%/<ë;3C2(9wA>1)]&àcukh0f"
print(a)
melange = "".join(random.sample(a, len(a)))
print(melange)