with open('code.txt', 'r', encoding='utf-8') as f:
    code_list = f.readlines()
    k = """ " """
    start = """ '<pre><code class="language-python">' """
    end = """ '</code></pre>' """
    with open("htmlcode.txt", "w") as file:
        for i in code_list:
            file.write(start + k + i.replace("\n", "") + k + end + "\n")
