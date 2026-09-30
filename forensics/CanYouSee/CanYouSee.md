# CanYouSee

## Approach
We recieve an unknown zip file on starting the chall. My first instinct was to run file and binwalk on it to scan for any hidden files. On 
finding no such hidden files, I extracted the zip and found a JPEG file. I uploaded the JPEG file on Aperi'Solve. In the exiftool section, 
I found an attribution URL in base64. On decoding it, I found the flag.

## Solution
Images are uploaded under the images folder

## Flag
picoCTF{ME74D47A_HIDD3N_b32040b8}

## Takeaway
Exiftool is a useful tool to find hidden flags