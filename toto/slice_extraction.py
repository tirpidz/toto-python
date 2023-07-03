import argparse
import traceback

import nibabel as nib


def slice_extraction(data_fname: str, slice_number: int, output_slice_fname: str):
    iamge = nib.load(data_fname)
    sliced_image = iamge.slicer[
        :, :, slice_number - 1 : slice_number
    ]  # since the voxel are zero based & the slice number are 1 based indexes.
    nib.save(sliced_image, output_slice_fname)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            prog="slice extraction", description="extract a slice from a nii 3D tensor"
        )

        parser.add_argument(
            "--data", help="the absolute filename of the nii data file", required=True
        )
        parser.add_argument(
            "--slice_number",
            type=int,
            help="the slice number to extract. Tthe index used will be zero based (i.e.: slice - 1)",
            required=True,
        )
        parser.add_argument(
            "--output",
            help="the absolute filename of the output slice nii file",
            required=True,
        )

        args = parser.parse_args()

        slice_extraction(
            data_fname=args.data,
            slice_number=args.slice_number,
            output_slice_fname=args.output,
        )
    except:
        print(traceback.format_exc())
        print("slice extraction failed")
        exit(1)

    print("slice sucessfully extracted")
