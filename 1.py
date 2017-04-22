#-*-coding:utf-8-*-
import tkinter
from tkinter import ttk
from tkinter import filedialog
import h5py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

root = tkinter.Tk()

file_path = tkinter.StringVar()
data_shape = tkinter.StringVar()
lable_shape = tkinter.StringVar()
data_content = tkinter.StringVar()
label_content = tkinter.StringVar()
label_kind = tkinter.StringVar()
select_show_index = tkinter.StringVar()


data = []

file_path.set('file_path')

def read_data(data):
	global data_content
	data_shape = data.shape
	for i in range(data_shape[0]):
		for j in range(data_shape[1]):
			data_content = str(data[i][j])

def open_h5df_file():
	global file_path
	global data_shape
	global lable_shape
	global data

	r = filedialog.askopenfilename(title='打开文件',filetypes=[('All Files','*.hdf5 *.h5')])
	file = h5py.File(r)
	tmp = file['label'][:]
	data =file['data'][:]

	file_path.set(r)
	data_shape.set(file['data'].shape)
	lable_shape.set(file['label'].shape)
	label_kind.set(len(set(tmp.reshape(len(tmp),))))
	#read_data(file['data'])
	#read_label(file['label'])

def show_3D():
	tmp = data.shape
	tmp_index_data = data[int(select_show_index.get())]
	x = list()
	y = list()
	z = list()
	for j in range(tmp_index_data.shape[0]):
		print(tmp_index_data[j])
		x.append(float(tmp_index_data[j][0]))
		y.append(float(tmp_index_data[j][1]))
		z.append(float(tmp_index_data[j][2]))
	
	ax = plt.subplot(111,projection='3d')
	ax.scatter(x,y,z)
	plt.show()		


mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0,row=0,sticky=(tkinter.N,tkinter.W,tkinter.E,tkinter.S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)



root.minsize(400,400)
ttk.Label(mainframe,textvariable=file_path).grid(column=0,row=1)
ttk.Button(mainframe,text='打开文件',command=open_h5df_file).grid(column=3,row=1)

ttk.Label(mainframe,text='数据维数').grid(column=0,row=2)
ttk.Label(mainframe,textvariable=data_shape).grid(column=2,row=2)

ttk.Label(mainframe,text='标签维数').grid(column=0,row=3)
ttk.Label(mainframe,textvariable=lable_shape).grid(column=2,row=3)

#ttk.Label(mainframe,text='数据内容').grid(row=4,column=1)
#ttk.Label(mainframe,textvariable=data_content).grid(row=4,column=2)


# ttk.Label(mainframe,text='标签内容').grid(row=5,column=1)
# tkinter.Text(mainframe).grid(row=5,column=2)

ttk.Label(mainframe,text='种类个数').grid(row=4,column=0)
ttk.Label(mainframe,textvariable=label_kind).grid(row=4,column=2)



ttk.Label(mainframe,text='要显示的文件').grid(row=5,column=0)
entry1 = ttk.Entry(mainframe,textvariable=select_show_index).grid(row=5,column=1)
ttk.Button(mainframe,text='确定',command=show_3D).grid(row=5,column=2)

root.mainloop()
