import instaloader
ig = instaloader.instaloader()
dp = input("enter the username:")
ig.download_profile(dp,profile_pic_only=True)