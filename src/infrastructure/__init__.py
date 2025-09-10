from flask import Flask, Blueprint

app = Flask(__name__)
infra_bp = Blueprint('infra', __name__)

from .routes import *
from .agents import UserAgent, GuestAgent, NutritionExpertAgent, PlannerAgent, AdminAgent

__all__ = ['app', 'infra_bp', 'UserAgent', 'GuestAgent', 'NutritionExpertAgent', 'PlannerAgent', 'AdminAgent']