import argparse
import traceback

import dipy.reconst.dti as dti
import numpy as np
from dipy.core.gradients import gradient_table
from dipy.io.gradients import read_bvals_bvecs
from dipy.io.image import load_nifti, save_nifti
from dipy.reconst.dti import fractional_anisotropy
from dipy.segment.mask import median_otsu


def FA_extraction(
    data_fname: str, bval_fname: str, bvec_fname: str, output_fa_fname: str
):
    data, affine = load_nifti(data_fname)
    bvals, bvecs = read_bvals_bvecs(bval_fname, bvec_fname)
    gtab = gradient_table(bvals, bvecs)

    maskdata, mask = median_otsu(
        data,
        vol_idx=range(0, data.shape[3]),
        median_radius=3,
        numpass=1,
        autocrop=True,
        dilate=2,
    )

    tenmodel = dti.TensorModel(gtab)
    tenfit = tenmodel.fit(maskdata)

    FA = fractional_anisotropy(tenfit.evals)
    FA[np.isnan(FA)] = 0

    save_nifti(
        output_fa_fname,
        FA.astype(np.float32),
        affine,
    )


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            prog="FA extraction", description="extract the full FA tensor"
        )

        parser.add_argument(
            "--data", help="the absolute filename of the nii data file", required=True
        )
        parser.add_argument(
            "--bval", help="the absolute filename of the bval file", required=True
        )
        parser.add_argument(
            "--bvec", help="the absolute filename of the bvec file", required=True
        )
        parser.add_argument(
            "--output",
            help="the absolute filename of the output FA tensor nii file",
            required=True,
        )

        args = parser.parse_args()

        FA_extraction(
            data_fname=args.data,
            bval_fname=args.bval,
            bvec_fname=args.bvec,
            output_fa_fname=args.output,
        )
    except:
        print(traceback.format_exc())
        print("FA tensor extraction failed")
        exit(1)

    print("FA tensor sucessfully extracted")
