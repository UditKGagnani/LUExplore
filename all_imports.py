import os
import re
from collections import defaultdict

import cv2
import numpy as np
import pandas as pd
import spacy
import tensorflow as tf
from flask import Flask, render_template, request
from keras.applications.vgg19 import preprocess_input
from keras.models import load_model
from keras.preprocessing import image
from keras.utils import to_categorical
from lightgbm import LGBMRegressor
from newsanalysis import sentiment_score
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor, StackingRegressor, VotingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from textblob import TextBlob

from catboost import CatBoostRegressor
from foodrecognition import predict_with_vgg_model
from houseprice import get_price
from itinerarygenerator import generate_itinerary
from xgboost import XGBRegressor
