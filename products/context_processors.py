from .models import Category

def nav_categories(request):
    
    return {
        'all_categories': Category.objects.all() 
    }
# userProfile/context_processors.py

from Accounts.models import userprofile

def user_profile(request):
    if request.user.is_authenticated:
        try:
            profile = userprofile.objects.get(
                user_profile_relation=request.user
            )
            return {"profile": profile}
        except userprofile.DoesNotExist:
            pass

    return {"profile": None}











