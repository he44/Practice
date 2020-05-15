## Practice

### Write the following into that file, one line at a time 

```bash
    echo "#\!/bin/sh" > semester
    echo "curl --head --silent https://missing.csail.mit.edu" >> semester
```

### Execute the file

```bash
    sh semester
```
will work, but ```./semester``` won't. 
Probably because we don't have "x" permission to semester?

```bash
    chmod +x semester
```

chmod can give "x" priviledge. "change mode". After this, the ```./semester``` will work

```bash
./semester | grep -i last-modified| cut -f 2- -d ' '
```

- grep finds the line with "last-modified", ```-i``` indicates ignoring case

- ```cut``` is kind of like "split" method in Python?

    - ```-f 2-``` gets every field starting from the second one (1-index)

    - ```-f2``` gives the second field

    - ```-d ' '``` uses space as delimeter, somehow I cannot use = as the course note suggests
