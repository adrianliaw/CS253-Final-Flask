from flask import Flask, render_template, redirect, request, session
from flask.ext.pymongo import PyMongo
from werkzeug.routing import BaseConverter
from datetime import datetime
from bson.objectid import ObjectId
import markdown2, re, random, hashlib, string, uuid, os