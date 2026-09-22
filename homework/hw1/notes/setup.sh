mkdir backup_check
curl -o holmes.txt https://www.gutenberg.org/cache/epub/1661/pg1661.txt
echo "downloaded"
ls -l
# ANSWER step 1: rmdir is only for empty directories, while rm -r can remove non-empty directories. Needed to use rm -r because rmdir couldn't find the file.