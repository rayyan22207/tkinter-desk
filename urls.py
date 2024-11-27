BASE_URL = "http://127.0.0.1:8000/api"  


def get_meeps_url():
    """Returns the URL for the list/create meeps endpoint."""
    return f"{BASE_URL}/meeps/"

def get_meep_detail_url(meep_id):
    """Returns the URL for a specific meep's details."""
    return f"{BASE_URL}/meeps/{meep_id}/"

def get_profile_url(profile_id):
    """Returns the URL for a specific profile."""
    return f"{BASE_URL}/profile/{profile_id}/"

def get_follow_unfollow_url(profile_id):
    """Returns the URL to follow/unfollow a profile."""
    return f"{BASE_URL}/profile/follow/{profile_id}/"

def get_search_meeps_url():
    """Returns the URL for searching meeps."""
    return f"{BASE_URL}/meeps/search/"

def get_meep_like_url(meep_id):
    """Returns the URL to like/unlike a meep."""
    return f"{BASE_URL}/meeps/{meep_id}/like/"
