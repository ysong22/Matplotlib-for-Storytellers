fig, ax = plt.figure(), plt.axes()
x = np.linspace(-3,3,200)
pdf_y = stats.norm.pdf(x)
cdf_y = stats.norm.cdf(x)
ax.plot(x,pdf_y, label = 'PDF')
ax.plot(x,cdf_y, label = 'CDF')
ax.legend()