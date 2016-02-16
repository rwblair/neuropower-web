import numpy as np
import scipy.ndimage as nd
from nibabel import save, Nifti1Image

def _cone3d(shape, ij, pos, ampli, width):
    """Define a cone of the proposed grid
    """
    temp = np.zeros(shape)
    pos = np.reshape(pos, (1, 3))
    dist = np.sqrt(np.sum((ij - pos) ** 2, axis=1))
    codi = (width - dist) * (dist < width) / width
    temp[ij[:, 0], ij[:, 1], ij[:, 2]] = codi * ampli
    return temp

def surrogate_3d_dataset(n_subj=1, shape=(20, 20, 20), mask=None,
                         sk=1.0, noise_level=1.0, pos=None, ampli=None,
                         spatial_jitter=1.0, signal_jitter=1.0,
                         width=5.0, out_text_file=None, out_image_file=None,
                         seed=False):
    """Create surrogate (simulated) 3D activation data with spatial noise.  From: https://github.com/nipy/nipy/blob/master/nipy/labs/utils/simul_multisubject_fmri_dataset.py
    Parameters
    -----------
    n_subj: integer, optionnal
        The number of subjects, ie the number of different maps
        generated.
    shape=(20,20,20): tuple of 3 integers,
         the shape of each image
    mask=None: Nifti1Image instance,
        referential- and mask- defining image (overrides shape)
    sk: float, optionnal
        Amount of spatial noise smoothness.
    noise_level: float, optionnal
        Amplitude of the spatial noise.
        amplitude=noise_level)
    pos: 2D ndarray of integers, optionnal
        x, y positions of the various simulated activations.
    ampli: 1D ndarray of floats, optionnal
        Respective amplitude of each activation
    spatial_jitter: float, optionnal
        Random spatial jitter added to the position of each activation,
        in pixel.
    signal_jitter: float, optionnal
        Random amplitude fluctuation for each activation, added to the
        amplitude specified by ampli
    width: float or ndarray, optionnal
        Width of the activations
    out_text_file: string or None, optionnal
        If not None, the resulting array is saved as a text file with the
        given file name
    out_image_file: string or None, optionnal
        If not None, the resulting is saved as a nifti file with the
        given file name.
    seed=False:  int, optionnal
        If seed is not False, the random number generator is initialized
        at a certain value
    Returns
    -------
    dataset: 3D ndarray
        The surrogate activation map, with dimensions ``(n_subj,) + shape``
    """
    if seed:
        nr = np.random.RandomState([seed])
    else:
        import numpy.random as nr

    if mask is not None:
        shape = mask.shape
        mask_data = mask.get_data()
    else:
        mask_data = np.ones(shape)

    ijk = np.array(np.where(mask_data)).T
    dataset = []

    # make the signal
    for s in range(n_subj):
        data = np.zeros(shape)
        lampli = []
        if pos is not None:
            if len(pos) != len(ampli):
                raise ValueError('ampli and pos do not have the same len')
            lpos = pos + spatial_jitter * nr.randn(1, 3)
            lampli = ampli + signal_jitter * nr.randn(np.size(ampli))
        for k in range(np.size(lampli)):
            data = np.maximum(data, _cone3d(shape, ijk, lpos[k], lampli[k],
                                            width))

        # make some noise
        noise = nr.randn(shape[0], shape[1], shape[2])

        # smooth the noise
        noise = nd.gaussian_filter(noise, sk)
        noise *= noise_level / np.std(noise)

        # make the mixture
        data += noise
        data[mask_data == 0] = 0
        dataset.append(data)

    dataset = np.array(dataset)
    if n_subj == 1:
        dataset = dataset[0]

    if out_text_file is not None:
        dataset.tofile(out_text_file)

    if out_image_file is not None:
        save(Nifti1Image(dataset, np.eye(4)), out_image_file)

    return dataset
