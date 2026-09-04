import json
from pathlib import Path


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET_ROOT = PROJECT_ROOT / "dataset" / "1"


# COCO category IDs
# 1 = space-empty
# 2 = space-occupied
CATEGORY_MAP = {
    1: 0,
    2: 1,
}


def convert_split(split):
    split_dir = DATASET_ROOT / split
    annotation_file = split_dir / "_annotations.coco.json"

    with open(annotation_file, "r") as f:
        coco = json.load(f)

    images = {image["id"]: image for image in coco["images"]}

    annotations_by_image = {}

    for annotation in coco["annotations"]:
        image_id = annotation["image_id"]

        if annotation["category_id"] not in CATEGORY_MAP:
            continue

        annotations_by_image.setdefault(image_id, []).append(annotation)

    converted = 0

    for image_id, image in images.items():
        image_name = Path(image["file_name"]).stem
        label_file = split_dir / f"{image_name}.txt"

        width = image["width"]
        height = image["height"]

        lines = []

        for annotation in annotations_by_image.get(image_id, []):
            category_id = annotation["category_id"]
            class_id = CATEGORY_MAP[category_id]

            x, y, box_width, box_height = annotation["bbox"]

            # Convert COCO bbox:
            # x, y, width, height
            #
            # into YOLO format:
            # center_x, center_y, width, height
            x_center = x + box_width / 2
            y_center = y + box_height / 2

            x_center /= width
            y_center /= height
            box_width /= width
            box_height /= height

            lines.append(
                f"{class_id} "
                f"{x_center:.6f} "
                f"{y_center:.6f} "
                f"{box_width:.6f} "
                f"{box_height:.6f}"
            )

        label_file.write_text("\n".join(lines))
        converted += 1

    print(f"{split}: converted {converted} images")


if __name__ == "__main__":
    for split in ["train", "valid", "test"]:
        convert_split(split)

    print("COCO to YOLO conversion complete!")