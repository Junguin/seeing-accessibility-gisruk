from zensvi.transform import ImageTransformer
from tqdm import tqdm

for i in tqdm(range(1, 76)):
    print(f'Running transformation for Batch {i}')

    dir_input = f"/mnt/home/yujun/data/liverpool_gsv_100m_gisruk/gsv_panorama/batch_{i}"
    dir_output = f"/mnt/home/yujun/data/liverpool_gsv_100m_gisruk/gsv_transformed/batch_{i}"

    image_transformer = ImageTransformer(
        dir_input=dir_input, 
        dir_output=dir_output
    )
    image_transformer.transform_images(
        style_list="perspective",  # list of projection styles in the form of a string separated by a space
        FOV=90,  # field of view
        theta=90,  # angle of view (horizontal)
        phi=0,  # angle of view (vertical)
        aspects=(1, 1),  # aspect ratio
        show_size=1024,  # size of the image to show (i.e. scale factor)
        use_upper_half=False,  # use the upper half of the image for sky view factor calculation
    )