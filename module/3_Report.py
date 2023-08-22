import streamlit as st 
from module.Home import face_rec
#st.set_page_config(page_title='Reporting',layout='wide')
st.subheader('Reporting')


# Retrive logs data and show in Report.py
# extract data from redis list
name = 'attendance:logs'
def load_logs(name,end=-1):
    logs_list = face_rec.r.lrange(name,start=0,end=end) # extract all data from the redis database
    return logs_list

    

# tabs to show the info
tab1, tab2 ,tab3= st.tabs(['Registered Data','Logs','Delete Data'])

with tab1:
    if st.button('Refresh Data'):
        # Retrive the data from Redis Database
        with st.spinner('Retriving Data from Redis DB ...'):    
            redis_face_db = face_rec.retrive_data(name='academy:register')
            st.dataframe(redis_face_db[['Name','Role']])
    
    
    
    

with tab2:
    if st.button('Refresh Logs'):
        st.write(load_logs(name=name))
    if st.button('Download Logs'):
        logs_list = face_rec.r.lrange(name,start=0,end=-1)
        with open(r'C:\Users\manoj\Desktop\@-@\project\FYP\Attendance System with Face Recognition\Notes\4_attendance_app\logs.txt','w') as fp:
            for item in logs_list:
                # write each item on a new line
                item = str(item, 'UTF-8')
                item = item.replace("@"," ",2)
                fp.write("%s\n" % item)
                
            if len(logs_list) > 0:
                st.success("Logs Downloaded Successfully")
            else:
                st.error("Logs is Empty")

    if st.button("Delete Logs"):
        ret_val = face_rec.r.lpop('attendance:logs')
        if face_rec.r.llen("attendance:logs")>0:
            st.success("Logs Deleted Successfully")
        elif face_rec.r.llen("attendance:logs")==0:
            st.error("Logs Completely deleted")

with tab3:
    #Delete the Data
    person_name = st.text_input(label='Name',placeholder='First & Last Name')
    role = st.selectbox(label='Select your Role',options=('Student',
                                                        'Teacher'))

    key = f"{person_name}@{role}"
        
    if st.button('Submit'):
        ret_val = face_rec.r.hdel('academy:register',key)
        if ret_val == 1:
            st.success(f'''{person_name}'s data deleted successfully''')
        if ret_val == 0:
            st.error(f'''{person_name}'s data not exists''')
        

        

