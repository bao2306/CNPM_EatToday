from fastapi import APIRouter, Depends
from controllers.auth_controller import AuthController
from controllers.course_controller import CourseController
from controllers.todo_controller import TodoController
from schemas.schemas import UserCreate, UserLogin, CourseCreate, CourseResponse, TodoCreate, TodoResponse

router = APIRouter()

@router.post("/auth/login")
async def login(user: UserLogin, controller: AuthController = Depends(AuthController)):
    return controller.login(user)

@router.post("/auth/register")
async def register(user: UserCreate, controller: AuthController = Depends(AuthController)):
    return controller.register(user)

@router.get("/courses/today", response_model=CourseResponse)
async def get_today_meal(controller: CourseController = Depends(CourseController)):
    return controller.get_random_meal()

@router.post("/courses", response_model=CourseResponse)
async def add_course(course: CourseCreate, controller: CourseController = Depends(CourseController)):
    return controller.add_course(course)

@router.get("/courses", response_model=list[CourseResponse])
async def get_all_courses(controller: CourseController = Depends(CourseController)):
    return controller.get_all_courses()

@router.post("/todos", response_model=TodoResponse)
async def add_todo(todo: TodoCreate, controller: TodoController = Depends(TodoController)):
    return controller.add_todo(todo)

@router.get("/todos", response_model=list[TodoResponse])
async def get_all_todos(controller: TodoController = Depends(TodoController)):
    return controller.get_all_todos()