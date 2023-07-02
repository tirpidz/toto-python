import numpy as np
from dipy.io.image import load_nifti, save_nifti
from dipy.io.gradients import read_bvals_bvecs
from dipy.core.gradients import gradient_table
import dipy.reconst.dti as dti
from dipy.segment.mask import median_otsu
from dipy.reconst.dti import fractional_anisotropy

data_fname = "/home/martin/src/toto-python/examples/input/dwi_b1000.nii.gz"
bval_fname = "/home/martin/src/toto-python/examples/input/bval_1000"
bvec_fname = "/home/martin/src/toto-python/examples/input/bvec_1000"

data, affine = load_nifti(data_fname)

bvals, bvecs = read_bvals_bvecs(bval_fname, bvec_fname)
gtab = gradient_table(bvals, bvecs)

print("data.shape (%d, %d, %d, %d)" % data.shape)

maskdata, mask = median_otsu(
    data, vol_idx=range(0, 47), median_radius=3, numpass=1, autocrop=True, dilate=2
)
print("maskdata.shape (%d, %d, %d, %d)" % maskdata.shape)

tenmodel = dti.TensorModel(gtab)

tenfit = tenmodel.fit(maskdata)

tensor_vals = dti.lower_triangular(tenfit.quadratic_form)

print("Computing anisotropy measures (FA, MD, RGB)")
FA = fractional_anisotropy(tenfit.evals)
FA[np.isnan(FA)] = 0
save_nifti(
    "/home/martin/src/toto-python/examples/output/tensor_fa.nii.gz",
    FA.astype(np.float32),
    affine,
)
