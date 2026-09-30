# RED

## Approach
We are given a PNG file. On uploading it into Aperi'Solve, we find that the exiftool has a special section called the poem. On looking at the first letter of each capitalized word. We get the hint to check LSB (least significant bit). Since I had zero clue how to do that, I asked AI how to do it and it told me to check the "b1,rgba,lsb,xy" value in the zsteg analysis on the PNG. The "b1,rgba,lsb,xy" value was encoded in base64. On decoding this, I obtained the flag.

## Solution
Images are in the images folder

## Flag
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}

## Takeaway
Learnt how to perform LSB analysis to check for hidden flags