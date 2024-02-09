import matplotlib.pyplot as mpl
x=[10,40,90,160]
y=[0.1,0.2,0.3,0.4]

fig,ax=mpl.subplots()

ax.plot(x,y,label="I-V graph",color="black")

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('N-shaped Curved Graph')
ax.legend()

# Display the graph
mpl.show()
