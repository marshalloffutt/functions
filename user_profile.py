# 8-13

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about user"""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile

user_profile = build_profile('marshall', 'offutt', 
                            location='nashville', 
                            field='programming')

print(user_profile)