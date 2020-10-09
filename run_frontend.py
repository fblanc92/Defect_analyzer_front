from Defect_analyzer_front.defect_app import create_app, db
import threading

app = create_app()  # nothing given as arg because Config class is default


def init_db():
    context = app.app_context()
    context.push()
    if 'users' not in db.get_engine(app=app, bind=None).table_names():
        db.create_all()


def start_frontend():
    app_thread = threading.Thread(target=app.run(host='0.0.0.0', port=5000)).start()



# if __name__ == '__main__':
    # init_db()
#     # start_backend()
    # start_frontend()
