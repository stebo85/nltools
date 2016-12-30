""" 
Basic Data Operations
=======================================

A simple example showing how to download a dataset from neurovault

"""

#########################################################################
# Download pain dataset from neurovault
# ---------------------------------------------------
# 
# Here we fetch the pain dataset used in Chang et al., 2015.  In this dataset
# there are 28 subjects with 3 separate beta images reflecting varying intensities
# of thermal pain (i.e., high, medium, low).  The data will be downloaded to ~/nilearn_data,
# and automatically loaded as a Brain_Data() instance.  The metadata will be stored in data.X.

from nltools.datasets import fetch_pain

data = fetch_pain()

#########################################################################
# Basic Brain_Data() Operations
# ---------------------------------------------------------
#
# Here are a few quick basic data operations.
# Find number of images in Brain_Data() instance

len(data)

#########################################################################
# Find the dimensions of the data.  images x voxels

data.shape()

#########################################################################
# We can use any type of indexing to slice the data

data[[1,6,2]]

#########################################################################
# Calculate the mean for every voxel over images

data.mean()

#########################################################################
# Methods can be chained.  Here we get the shape of the mean.

data.mean().shape()

#########################################################################
# Brain_Data instances can be added and subtracted

new = data[1]+data[2]

#########################################################################
# Brain_Data instances can be concatenated using the append method

new = new.append(data[4])

#########################################################################
# Any Brain_Data object can be written out to a nifti file

data.write('Tmp_Data.nii.gz')
	
#########################################################################
# Basic Brain_Data() Plotting
# ---------------------------------------------------------
#
# There are multiple ways to plot data.  First, Brain_Data() instances can be 
# converted to a nibabel instance and plotted using any plot method such as
# nilearn.

from nilearn.plotting import plot_glass_brain

plot_glass_brain(data.mean().to_nifti())

#########################################################################
# There is also a fast montage plotting method.  Here we plot the average image

data.mean().plot()
