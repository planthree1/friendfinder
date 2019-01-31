from django.http import JsonResponse
from friend_finder.utils import send_ok, check_parameters
import friend_finder.models as models


# Create your views here.
def get_all_user(request):
    a = models.User.objects.all()
    return JsonResponse({"Users": [u.get() for u in a]})


def get_id(request):
    try:

        user = models.User.objects.filter(installation_id=request.GET.get('installation_id')).first()

    except Exception as e:
        print(e)
        return JsonResponse({"Error": str(e)})

    return JsonResponse({"id": user.id})


def add_user(request):
    try:
        id = request.GET.get('installation_id', '')

        if models.User.objects.filter(installation_id=id).exists():
            raise Exception("User already exists")

        user = models.User()
        user.installation_id = id
        user.latitude = float(request.GET.get('latitude', '0'))
        user.longitude = float(request.GET.get('longitude', '0'))
        user.save()
    except Exception as e:
        print(e)
        return JsonResponse({"Error": str(e)})

    return send_ok()


def add_group(request):
    try:
        group = models.Group()
        group.name = request.GET.get('name', '')
        group.active = request.GET.get('active', 'True')
        group.save()
    except Exception as e:
        print(e)
        return JsonResponse({"Error": str(e)})

    return send_ok()


def update_coordinates(request):
    try:
        check_parameters(request, "installation_id", "latitude", "longitude")
        user = models.User.objects.filter(installation_id=request.GET.get('installation_id')).first()
        user.latitude = float(request.GET.get('latitude'))
        user.longitude = float(request.GET.get('longitude'))
        user.save()
    except Exception as e:
        print(e)
        return JsonResponse({"Error": str(e)})
    return send_ok()


def add_group_user(request):
    group_user = models.GroupUser()
    user = models.User.objects.filter(installation_id=request.GET.get('installation_id', '')).first()
    group = models.Group.objects.filter(name=request.GET.get('name', '')).first()

    group_user.group = group
    group_user.user = user
    group_user.save()
    return send_ok()


def get_group(request):
    try:
        if "id" not in request.GET:
            raise Exception("ID parameter not found")
        id=request.GET["id"]
        try:
            user = models.User.objects.filter(installation_id=id).first()
        except:
            raise Exception("user does not exist")


        try:
            group_user = models.GroupUser.objects.filter(user=user)
        except:
            raise Exception("user has no groups")

        result = {"Groups": [gu.group.get() for gu in group_user]}
    except Exception as e:
        print(e)
        return JsonResponse({"Error": str(e)})

    return JsonResponse(result)


def get_user_from_group(request):
    try:
        if "id" not in request.GET:
            raise Exception("ID parameter not found")
        id=request.GET["id"]
        try:
            group = models.Group.objects.filter(name=id).first()
        except:
            raise Exception("group does not exist")


        try:
            group_user = models.GroupUser.objects.filter(group=group)
        except:
            raise Exception("emtpy group")

        result = {"users": [gu.user.get() for gu in group_user]}
    except Exception as e:
        print(e)
        return JsonResponse({"Error": str(e)})

    return JsonResponse(result)


def delete_group(request):
    try:
        if "name" not in request.GET:
            raise Exception("ID parameter not found")
        name=request.GET["name"]
        try:
            group = models.Group.objects.filter(name=name).delete()
            group.save()
        except:
            raise Exception("group does not exist")

    except Exception as e:
        print(e)
        return JsonResponse({"Error": str(e)})

    return send_ok()
