from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student


class Face_Recognition_System:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        # first image
        img=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\smart-attendance.jpg")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)    
        f_lbl.place(x=0,y=0,width=500,height=150)
        
        
        # second image
        img1=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\facialrecognition.png")
        img1=img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)    
        f_lbl.place(x=500,y=0,width=500,height=150)
       
       
        # third image
        img2=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\facial-recognition_0.jpg")
        img2=img2.resize((500,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)    
        f_lbl.place(x=1000,y=0,width=550,height=150)
        
        
        # bg image
        img3=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\bg_face.jpg")
        # img3=img3.resize((100,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)    
        bg_img.place(x=0,y=100,width=1300,height=700)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman",35,"bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=1,width=1245,height=45)
        
        
        # -------------Functions buttons-----------------
        def student_details():
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)
        
        
        
        # 1. student button
        img4=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        # command=self.student_details
        b1=Button(bg_img,command=student_details,image=self.photoimg4,cursor="hand2")
        b1.place(x=100,y=50,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=student_details,cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=100,y=250,width=220,height=40)
        
        
        
        
        # 2. detect face button
        img5=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img, image=self.photoimg5,cursor="hand2")
        b1.place(x=375,y=50,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=375,y=250,width=220,height=40)
       
       
       
        # 3. Attendance face button
        img6=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\smart-attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img, image=self.photoimg6,cursor="hand2")
        b1.place(x=650,y=50,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=650,y=250,width=220,height=40)
       
       
       
        # 4. Help button
        img7=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img, image=self.photoimg7,cursor="hand2")
        b1.place(x=925,y=50,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=925,y=250,width=220,height=40)
        
        
        
        # Train button
        img8=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\Train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img, image=self.photoimg8,cursor="hand2")
        b1.place(x=100,y=300,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=100,y=500,width=220,height=40)
        
        
        
        # Photos button
        img9=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\images.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img, image=self.photoimg9,cursor="hand2")
        b1.place(x=375,y=300,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=375,y=500,width=220,height=40)
        
        
        
        #  Developer button
        img10=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img, image=self.photoimg10,cursor="hand2")
        b1.place(x=650,y=300,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=650 ,y=500,width=220,height=40)
        
        
        
        
        # Exit button
        img11=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img, image=self.photoimg11,cursor="hand2")
        b1.place(x=925,y=300,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=925,y=500,width=220,height=40)
       

            
       
            

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()