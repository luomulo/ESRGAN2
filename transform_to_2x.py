from PIL import Image
import os

def double_image_size(input_folder, output_folder):
    # 如果输出文件夹不存在，则创建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 确保处理的是图像文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 构建文件的完整路径
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # 打开图像文件
            with Image.open(input_path) as img:
                # 获取原始尺寸
                width, height = img.size
                # 计算新尺寸
                new_size = (width * 2, height * 2)
                # 调整图像尺寸
                resized_img = img.resize(new_size, Image.LANCZOS)
                # 保存调整后的图像
                resized_img.save(output_path)
                print(f"Resized {filename} from {width}x{height} to {new_size[0]}x{new_size[1]}")

if __name__ == "__main__":
    input_folder = r"C:\Users\wangweijia\Desktop\sourcebook_hr"  # 替换为您的输入文件夹路径
    output_folder = r"C:\Users\wangweijia\Desktop\New folder (2)"  # 替换为您的输出文件夹路径

    double_image_size(input_folder, output_folder)
