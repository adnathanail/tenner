def group_processor(request):
 staffGroup = request.user.groups.filter(name="Staff").count() == 1
 return {'group': staffGroup}
