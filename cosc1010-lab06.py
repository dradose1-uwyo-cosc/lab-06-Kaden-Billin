# Kaden Billin
# UWYO COSC 1010
# 10-17-24
# Lab 06
# Lab Section: 12
# Sources, people worked with, help given to: 
# your
# comments
# here


random_string = """
jppamiqxegokaizvkyawwurhewtcxohryzptznyuedhhmawpic
pkzwuiorngdfcsgqnlyifzyaivehpiyszykqprbcsobygzhadd
yfddbulxmcnyvqhesmnybyuhxjqqmhdxwhcselasiayqhctnlw
hakethjahqnvjdowhlyzosemxkbenestxgvgncmffkcxldcmkl
itclmqdhrbdgzwtvdxwedcknbyaecvttjphtxubvhwvcvjqayy
almxuxjbcmznnzekptfzbldsjwpvringlmalwufvlppeiendur
dyophftqjkghhncwxoksqaqnpueudpygiytqgpcgjqsjbtbpzi
vaeczmyicnednjjoxkpnjmpfbgyjnbfjlweqqppodfxfzzwkuf
rldgryyhceuikimoavosuzuozthmatcgxcmkxnaxmsevkcumby
spiajlbycvrluxdkfavxidzalxuixqkxiybhfuqhcvmrhzbzse
idjwgwdwgfkyreozkyoxdvhixfejxjfgkkgobescboyfshiovu
fxdyvfsnmjzsphgmtldlaoehofcspzujghcdcxzggvunpbtglr
topplmkviuewwpoaplmbpgejmymxbyzzwbnujrlysszmxkjerb
zpiewqvgopvhmmcgwcyvxvwhdvfgsrybcozhdtwujhdbxzznkc
ergcqbetpgwrejuluqfxchlihunzbcdwboysjqenjxzbgqbycx
dybxpyztjyxpkqfvxullzkedpkjjobhymfinpvprxejktyrpai
ehjgwahpquzcmvclatdfcmattavoehnhnzveoxwnmnptxbvxto
gpcobgzdhsjevhcohkltftmrqkosknkxeylhqxkkctbnusijgr
uvecpbqmylqdaohkfaqbgeokyyipumjuaaayikdzyxfrpaieyo
uxiosjwioebsjtslblfurgcodtyaggzovzfnnyjngawiwbbtqi
kqqhnkwheolpqzasmsmbxqkeiqvogquobphewznfsnlkkizhca
cbiyvxpmjxywqvzqtshfvnfbusphggexfqzepsrduvtovdsknl
ztyuwugprkhbmktfvrenbmqgdjwnkeugtojrpqfmjhtrlcqcpq
pwsguedzgvktpwbqkhkueymjtxbvzmdfjopzkygujrjdtogssg
cxczryuqhhgjlpultkoffescpzyjrfqqabnhkfdnhkylpjamxk
uxidjkqdrkxqjqjtflebvwhcvqjciykzhrvppvxhvpedgznwty
kujglixooczrhxziasjxddfcghzlwrqcyiilpruhdfvitewxzg
dzcvmvnoskchscgoqfsojfvahlwkrslzeirlblseplcmpmbmum
ibrdamvqfstydtjopdkdcbnnmpifxckozyxzluhcqbqtpismog
ulufaajxvuizvdzioxfvypxovptkibcrjvfidomejknuggfrtp
kptwffersvqjknemkejsgspckwqisdcliuezhbeqpwgrjcqajl
huobykkbujmyuuinbwdklqfhvakyozzsxghfyownjjwqtkxgkf
ipdbjzxfogozstfsektujsvklrvecditiectuvtfibohmxxzna
cpqzeoburtquuizhypugnkvuwbdxnraareqkofhfjobrpcsuxq
nbafxlkuafbfsiuyrxdusqyasqyrwhdjrukgxdackumvairlgn
fjhenwbrdghbevgqbybpwncclolgqyuhallbqtzdywbvlzwtil
jctmsxjortnxvlbhuhkblppewjhqjzxrwgftlturxjuwfoaqpp
sgfnxwxolkbrpdmpniitoljzaxabgtnelrmryetxqypwrjdyjc
zipwbdpbazxpesmrcfuikeamtlsrgxrhzfytecenyydeemrhxj
gmdruhillntvpadzbroyygydpmonwuakruvxbdrqhtrjvoqsin
gjbarzvuqplmsmbwtqfghteoknbxmaokwlqqfoblmzsxczjzfj
mzmawtarjdtgongqqufhhdjwcinhlxcsgoltjycxrkloqozxoi
crlfmgflzzxgiiliqlksxyaydsohhahzxtsufzppftvgbpsdlx
ertfmbothijzrrdvfrnsohnwulcxvcvxngvmznhazxrgdsugij
fracotpirvqemsiuualpkpvtmtgchmowkmvoolrjfblrtwkmtr
xhawucytgwlahddkhxxfublukkdldpovqokntydhzzrxiisdwu
ujrkoewqoflyebogbwgdhriwkkoiofwtjlhxxtmzkklzbcmxhv
lrslowamkcwolbcgfkfciegdwqskuazxnycqkkggzsowcmafay
ibmkdwkqmdkjesqnjiqpijixbwjhenmsrrlpcseliiajlvcaac
zkdenxczyooloczcaahnkehbwimvieedpdlqfafbqvxvfmvabd
"""
random_string = random_string.replace("\n","") #remove all newline characters
print(len(random_string)) # Print out the size for reference 

# Above is a string with 2500 characters.
# Create a program that goes through and counts the occurrence of each character, excluding \n using a  dictionary
# Output each letter and its corresponding occurrence in alphabetical order
# Output which letter occurred the most 
# Output which letter occurred the least 
# Output what the percentage of the string each character is, again in alphabetical
letter_values = {}
aoccurances = 0
boccurances = 0
coccurances = 0
doccurances = 0
eoccurances = 0
foccurances = 0
goccurances = 0
hoccurances = 0
ioccurances = 0
joccurances = 0
koccurances = 0
loccurances = 0
moccurances = 0
noccurances = 0
ooccurances = 0
poccurances = 0
qoccurances = 0
roccurances = 0
soccurances = 0
toccurances = 0
uoccurances = 0
voccurances = 0
woccurances = 0
xoccurances = 0
yoccurances = 0
zoccurances = 0

for letter in random_string:
    if letter == "a":
        aoccurances = (aoccurances+1)
        letter_values["a occurances"] = aoccurances
for letter in random_string:
    if letter == "b":
        boccurances = (boccurances+1)
        letter_values["b occurances"] = boccurances
for letter in random_string:
    if letter == "c":
        coccurances = (coccurances+1)
        letter_values["c occurances"] = coccurances
for letter in random_string:
    if letter == "d":
        doccurances = (doccurances+1)
        letter_values["d occurances"] = doccurances
for letter in random_string:
    if letter == "e":
        eoccurances = (eoccurances+1)
        letter_values["e occurances"] = eoccurances
for letter in random_string:
    if letter == "f":
        foccurances = (foccurances+1)
        letter_values["f occurances"] = foccurances
for letter in random_string:
    if letter == "g":
        goccurances = (goccurances+1)
        letter_values["g occurances"] = goccurances
for letter in random_string:
    if letter == "h":
        hoccurances = (hoccurances+1)
        letter_values["h occurances"] = hoccurances
for letter in random_string:
    if letter == "i":
        ioccurances = (ioccurances+1)
        letter_values["i occurances"] = ioccurances
for letter in random_string:
    if letter == "j":
        joccurances = (joccurances+1)
        letter_values["j occurances"] = joccurances
for letter in random_string:
    if letter == "k":
        koccurances = (koccurances+1)
        letter_values["k occurances"] = koccurances
for letter in random_string:
    if letter == "l":
        loccurances = (loccurances+1)
        letter_values["l occurances"] = loccurances
for letter in random_string:
    if letter == "m":
        moccurances = (moccurances+1)
        letter_values["m occurances"] = moccurances
for letter in random_string:
    if letter == "n":
        noccurances = (noccurances+1)
        letter_values["n occurances"] = noccurances
for letter in random_string:
    if letter == "o":
        ooccurances = (ooccurances+1)
        letter_values["o occurances"] = ooccurances
for letter in random_string:
    if letter == "p":
        poccurances = (poccurances+1)
        letter_values["p occurances"] = poccurances
for letter in random_string:
    if letter == "q":
        qoccurances = (qoccurances+1)
        letter_values["q occurances"] = qoccurances
for letter in random_string:
    if letter == "r":
        roccurances = (roccurances+1)
        letter_values["r occurances"] = roccurances
for letter in random_string:
    if letter == "s":
        soccurances = (soccurances+1)
        letter_values["s occurances"] = soccurances
for letter in random_string:
    if letter == "t":
        toccurances = (toccurances+1)
        letter_values["t occurances"] = toccurances
for letter in random_string:
    if letter == "u":
        uoccurances = (uoccurances+1)
        letter_values["u occurances"] = uoccurances
for letter in random_string:
    if letter == "v":
        voccurances = (voccurances+1)
        letter_values["v occurances"] = voccurances
for letter in random_string:
    if letter == "w":
        woccurances = (woccurances+1)
        letter_values["w occurances"] = woccurances
for letter in random_string:
    if letter == "x":
        xoccurances = (xoccurances+1)
        letter_values["x occurances"] = xoccurances
for letter in random_string:
    if letter == "y":
        yoccurances = (yoccurances+1)
        letter_values["y occurances"] = yoccurances
for letter in random_string:
    if letter == "z":
        zoccurances = (zoccurances+1)
        letter_values["z occurances"] = zoccurances

#Tips and trick:
# You can iterate through strings like you would a list
# All characters are lowercase 
# Each letter will be PAIRED with its corresponding value 
# That is to say, this is a great use of dictionaries
    # You will  need to add the letter to the dictionary on first occurrence 
    # Then increment its corresponding count 


#Load all the elements into a dictionary
#Will need to first declare a dictionary 

# Output: each letter and its corresponding occurrence in alphabetical order

print(letter_values)
print("*"*75)

# Output which letter occurred the most 

for letter, value in letter_values.items():
    print(value)
most_occurred = ""
least_occurred = ""

print(f"The letter that occurred the most is {most_occurred}")
print("*"*75)
# Output which letter occurred the least 
print(f"The letter that occurred the most is {least_occurred}")
print("*"*75)

# Output what the percentage of the string each character is, again in alphabetical
