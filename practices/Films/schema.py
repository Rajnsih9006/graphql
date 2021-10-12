
# from typing_extensions import Required
# from typing_extensions import Required
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import EmailField
import graphene
from graphene.types import mutation
from graphene.types.scalars import ID
from graphene_django.types import ALL_FIELDS
# from graphene.types.mutation import Mutation
from graphql_auth import mutations
from graphql_auth.schema import UserQuery,MeQuery


from graphene_django import DjangoObjectType
from graphql_jwt.decorators import token_auth
from graphql_jwt.mutations import Verify
from .models import ExtendUser,MoviesName


class ExtenUserType(DjangoObjectType):
    class Meta:
        model = ExtendUser
class MoviesNameType(DjangoObjectType):
    class Meta:
        model = MoviesName 




class GenderTypeEnum(graphene.Enum):
    Male = "Male"
    Female = "Female" 
    
# class CreateUser(graphene.Mutation):
#     class Arguments:
#         email = graphene.String(required = True)
#         username=graphene.String()

#     user = graphene.Field(ExtenUserType)
#     success=graphene.Boolean()  

#     @staticmethod
#     def mutate(root,cls,email,username):
#         user = ExtendUser(email = email,username=username)
#         user.save()
#         return CreateUser(success = True)
                      


# class UpdateUser(graphene.Mutation):
#     class Arguments:
#         id=graphene.ID()
#         email=graphene.String()
#         username=graphene.String()

#     user = graphene.Field(ExtenUserType)
#     success=graphene.Boolean() 

#     @staticmethod
#     def mutate(root,info,username,id,email):
#         user=ExtendUser.objects.get(id=id)
#         user.email=email
#         user.username=username
#         user.save()
#         return UpdateUser(success=True)


# class DeleteUser(graphene.Mutation):
#     class Arguments:
#         id=graphene.ID()

#     user=graphene.Field(ExtenUserType)   
#     success=graphene.Boolean()

#     @staticmethod
#     def mutate(root,info,id):
#         user=ExtendUser.objects.get(id=id)
#         user.delete()
#         return DeleteUser(success=True)


class CreateMoviesName(graphene.Mutation):
    class Arguments:
        user_id=graphene.ID()
        actor=graphene.String()
        movies=graphene.String()
        gender=GenderTypeEnum()

    User = graphene.Field(MoviesNameType)
    success=graphene.Boolean() 
   


    
    @staticmethod
    def mutate(root,cls,actor,movies,gender,user_id):
        idd=ExtendUser.objects.get(id=user_id)
        user =MoviesName (actor_name =actor,movies_name=movies,gender=gender,user_id=idd) 
        user.save()
        return CreateMoviesName(success = True)


class UpdateMoviesName(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        actor=graphene.String()
        movies=graphene.String()
        

    User = graphene.Field(MoviesNameType)
    success=graphene.Boolean() 

    @staticmethod
    def mutate(root,info,actor,movies,id):
        idd=MoviesName.objects.get(id=id)
        idd.actor_name=actor
        idd.movies_name=movies
        idd.save()
        return UpdateMoviesName(success=True)


class DeleteMoviesName(graphene.Mutation):
    class Arguments:  
         id=graphene.ID()   
    user=graphene.Field(MoviesNameType)   
    success=graphene.Boolean()

    @staticmethod
    def mutate(root,info,id):
        idd=MoviesName.objects.get(id=id)
        idd.delete()
        return DeleteMoviesName(success=True)



class Query(graphene.ObjectType):
    by_id=graphene.List(ExtenUserType,id=graphene.ID())
    movies_name=graphene.List(MoviesNameType,movies_name=graphene.String())

    def resolve_by_id(self,info,id):
        return ExtendUser.objects.filter(id=id)
    def resolve_movies_name(self,info,movies_name):
        return MoviesName.objects.filter(movies_name=movies_name)

class AuthMutation(graphene.ObjectType):
    register=mutations.Register.Field()
    Verify_account=mutations.VerifyAccount.Field()
    token_auth=mutations.ObtainJSONWebToken.Field()
    send_password_reset_email=mutations.SendPasswordResetEmail.Field()
    password_reset=mutations.PasswordReset.Field() 


class Mutation(AuthMutation,graphene.ObjectType):
    # create_user = CreateUser.Field()
    # update_user=UpdateUser.Field() 
    # delete_user=DeleteUser.Field()
    Create_name=CreateMoviesName.Field()
    update_name=UpdateMoviesName.Field()
    delete_name=DeleteMoviesName.Field()



 
schema = graphene.Schema(mutation=Mutation,query=Query)