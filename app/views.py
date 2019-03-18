from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import ProfileForm
import datetime
from werkzeug.utils import secure_filename
import os
from app import db


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')



@app.route("/profile", methods=["GET", "POST"])
def profile():
    form = ProfileForm()
    if request.method == "POST" and form.validate_on_submit():
        photo = form.Pic.data
        name = form.firstName.data + " "+ form.lastName.data
        gender = form.gender.data
        email = form.email.data
        location = form.location.data
        bio = form.biography.data
        filename = secure_filename(photo.filename)
        phot.save(os.path.join(
            app.config["UPLOAD_FOLDER"],filename

        ))
        created_on = getDate()
        flash("SUCCESS")
        return redirect(url_for("home"))
    return render_template("profile.html", form=form)
        
