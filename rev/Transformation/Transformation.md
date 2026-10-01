# Transformation

## Approach
On opening the file, we recieved some chinese/korean looking text 慣慤敭祻ㄶ形楴獟楮獴㌴摟潦弸強㤰扡㌷敽. My first instinct was to use google translate to convert it back to english. However that did not yield anything. On asking claude what the description of the chall means, i got to know that each character in the given string is 2 ASCII characters combined into one.

## Solution
Looking at the code, we understand that they first convert each character of the flag to its number and then shift the first number by 8 bits, which is the equivalent of multiplying it by 256. This moves it into the high byte of the 16bit(2 byte) number and leaves the other number into the low byte position. Then we combine this 16 bit number into a single unicode characters and then concatenate them together. 

To reverse this process, we first convert each unicode character back into its 16 bit number, which is 4 hex digits. The first two hex digits are the high byte, which is the first flag character, and the last two hex digits are the low byte, which is the second flag character. For example, 慣 is 0x6163, where 0x61 is 'a' and 0x63 is 'c'. To get the high byte we shift the number to the right by 8, which undoes the left shift from the encoding, and to get the low byte we use a bitwise AND with 0xFF, which keeps only the last 8 bits. We then convert both bytes back to ASCII characters and concatenate them for every character in the string, thus giving us the flag. (I asked claude to write the code).

Screenshots are provided in the images picture.
Code to decrypt is in decrypt.py (slopped)

## Flag
academy{16_bits_inst34d_of_8_790ba37e}

## Takeaway
Chinese/Korean looking text often is a combination of 2 unicode characters.