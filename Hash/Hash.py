import os
import hashlib
import time
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
from pathlib import Path


class LanguageManager:
    def __init__(self):
        self.languages = {}
        self.current_lang = "zh-CN"
        self.load_languages()

    def load_languages(self):
        """加载所有语言文件"""
        lang_dir = Path("Languages")

        # 如果语言目录不存在，则直接使用内置中文
        if not lang_dir.exists():
            self.languages["zh-CN"] = self.get_default_zh_cn()
            return

        # 尝试加载中文语言包
        zh_cn_path = lang_dir / "zh-CN.json"
        if zh_cn_path.exists():
            try:
                with open(zh_cn_path, "r", encoding="utf-8") as f:
                    self.languages["zh-CN"] = json.load(f)
            except:
                self.languages["zh-CN"] = self.get_default_zh_cn()
        else:
            self.languages["zh-CN"] = self.get_default_zh_cn()

        # 尝试加载英文语言包
        en_us_path = lang_dir / "en-US.json"
        if en_us_path.exists():
            try:
                with open(en_us_path, "r", encoding="utf-8") as f:
                    self.languages["en-US"] = json.load(f)
                # 如果英文语言包存在，则使用英文
                self.current_lang = "en-US"
            except:
                # 英文语言包加载失败，继续使用中文
                pass

    def get_default_zh_cn(self):
        """返回内置的中文语言包"""
        return {
            "window_title": "文件哈希值计算工具",
            "status_ready": "就绪",
            "algorithm_frame": "选择哈希算法",
            "hash_algorithm_selected": "已选择哈希算法: {}",
            "single_file_tab": "计算文件哈希值",
            "compare_files_tab": "比较文件哈希值",
            "folder_hash_tab": "计算文件夹哈希值",
            "folder_compare_tab": "比较文件夹哈希值",
            "select_file": "选择文件",
            "browse": "浏览...",
            "calculate_hash": "计算哈希值",
            "result": "计算结果",
            "file_path": "文件路径: {}",
            "file_size": "文件大小: {} 字节 ({:.2f} MB)",
            "hash_algorithm": "哈希算法: {}",
            "time_taken": "计算耗时: {:.4f} 秒",
            "hash_value": "哈希值: \n{}",
            "select_folder": "选择文件夹",
            "calculate_folder_hash": "计算文件夹哈希值",
            "folder_path": "文件夹路径: {}",
            "total_files": "包含文件数: {}",
            "folder_size": "总大小: {} 字节 ({:.2f} MB)",
            "folder_hash": "文件夹哈希值: \n{}",
            "compare_files": "比较文件哈希值",
            "select_file1": "选择文件1",
            "select_file2": "选择文件2",
            "file1": "文件1: {}",
            "file2": "文件2: {}",
            "file1_hash": "文件1哈希值 ({}): \n{}",
            "file2_hash": "文件2哈希值 ({}): \n{}",
            "match_success": "✅ 两个文件的哈希值一致！",
            "match_fail": "❌ 两个文件的哈希值不一致！",
            "select_folder1": "选择文件夹1",
            "select_folder2": "选择文件夹2",
            "folder1": "文件夹1: {}",
            "folder2": "文件夹2: {}",
            "folder1_hash": "文件夹1哈希值 ({}): \n{}",
            "folder2_hash": "文件夹2哈希值 ({}): \n{}",
            "folder_match_success": "✅ 两个文件夹的哈希值一致！",
            "folder_match_fail": "❌ 两个文件夹的哈希值不一致！",
            "file_count_warning": "⚠️ 注意: 文件数量不同 (文件夹1: {}, 文件夹2: {})",
            "size_warning": "⚠️ 注意: 总大小不同 (文件夹1: {:.2f} MB, 文件夹2: {:.2f} MB)",
            "size_same_content_different": "- 文件数量和总大小相同，但内容不同",
            "file_count_different": "- 文件数量不同 (文件夹1: {}, 文件夹2: {})",
            "size_different": "- 总大小不同 (文件夹1: {:.2f} MB, 文件夹2: {:.2f} MB)",
            "processing": "正在处理: {} ({}/{})",
            "calculating_file_hash": "正在计算文件哈希值...",
            "calculating_folder_hash": "正在计算文件夹哈希值...",
            "comparing_files": "正在计算并比较文件哈希值...",
            "comparing_folders": "正在计算并比较文件夹哈希值...",
            "calculating_folder1": "正在计算第一个文件夹...",
            "calculating_folder2": "正在计算第二个文件夹...",
            "calculation_complete": "计算完成 - 耗时: {:.4f} 秒",
            "comparison_complete": "比较完成 - 总耗时: {:.4f} 秒",
            "folder_calculation_complete": "文件夹哈希计算完成 - 耗时: {:.2f} 秒",
            "folder_comparison_complete": "比较完成 - 总耗时: {:.2f} 秒",
            "calculation_failed": "计算失败",
            "folder_calculation_failed": "文件夹哈希计算失败",
            "comparison_failed": "比较失败",
            "file_selected": "已选择文件: {}",
            "folder_selected": "已选择文件夹: {}",
            "file_num_selected": "已选择文件{}: {}",
            "folder_num_selected": "已选择文件夹{}: {}",
            "error": "错误",
            "file_not_selected": "请先选择文件",
            "file_not_exist": "文件不存在: {}",
            "folder_not_selected": "请先选择文件夹",
            "folder_not_exist": "文件夹不存在: {}",
            "two_files_required": "请选择两个文件",
            "two_folders_required": "请选择两个文件夹",
            "same_file_error": "不能比较同一个文件",
            "same_folder_error": "不能比较同一个文件夹",
            "hash_calculation_error": "计算文件哈希值时出错: {}",
            "folder_hash_error": "计算文件夹哈希值时出错: {}",
            "exit_confirmation": "退出",
            "exit_message": "确定要退出程序吗？",
            "all_files": "所有文件"
        }

    def get(self, key, *args):
        """获取当前语言的文本，支持格式化参数"""
        try:
            text = self.languages[self.current_lang][key]
            if args:
                return text.format(*args)
            return text
        except KeyError:
            # 如果当前语言没有该键，尝试使用中文回退
            if self.current_lang != "zh-CN" and "zh-CN" in self.languages:
                try:
                    text = self.languages["zh-CN"][key]
                    if args:
                        return text.format(*args)
                    return text
                except:
                    return key
            return key


class HashCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.lang = LanguageManager()
        self.root.title(self.lang.get("window_title"))
        self.root.geometry("1000x800")
        self.root.resizable(True, True)

        # 设置默认哈希算法
        self.hash_algorithm = tk.StringVar(value="sha256")

        # 创建主框架
        self.main_frame = ttk.Frame(root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # 算法选择部分
        algo_frame = ttk.LabelFrame(self.main_frame, text=self.lang.get("algorithm_frame"), padding=10)
        algo_frame.pack(fill=tk.X, padx=10, pady=5)

        algorithms = [
            ("SHA-256", "sha256"),
            ("SHA-1", "sha1"),
            ("MD5", "md5"),
            ("SHA-512", "sha512")
        ]

        for i, (text, algo) in enumerate(algorithms):
            rb = ttk.Radiobutton(
                algo_frame,
                text=text,
                variable=self.hash_algorithm,
                value=algo,
                command=lambda: self.update_status(
                    self.lang.get("hash_algorithm_selected", self.hash_algorithm.get().upper()))
            )
            rb.grid(row=0, column=i, padx=10, pady=5, sticky=tk.W)

        # 创建标签页
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # 创建单个文件计算标签页
        self.create_single_file_tab()

        # 创建文件比较标签页
        self.create_compare_files_tab()

        # 创建文件夹哈希计算标签页
        self.create_folder_hash_tab()

        # 创建文件夹比较标签页
        self.create_folder_compare_tab()

        # 创建状态栏
        self.status_var = tk.StringVar(value=self.lang.get("status_ready"))
        self.status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # 设置样式
        self.set_style()

        # 绑定关闭事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def set_style(self):
        """设置UI样式并使用楷体字体"""
        style = ttk.Style()

        # 使用更大的楷体字体
        large_font = ("楷体", 12)
        bold_font = ("楷体", 12, "bold")
        fixed_font = ("楷体", 11)

        style.configure("TButton", padding=6, font=large_font)
        style.configure("TLabel", font=large_font)
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TNotebook", background="#f0f0f0")
        style.configure("TNotebook.Tab", padding=(10, 5), font=bold_font)
        style.configure("StatusBar.TLabel", background="#e0e0e0", font=large_font)
        style.configure("Title.TLabel", font=bold_font)

        self.status_bar.configure(style="StatusBar.TLabel")

        # 设置所有子控件的字体
        for widget in self.root.winfo_children():
            if isinstance(widget, (tk.Button, tk.Label, tk.Entry, tk.Radiobutton)):
                widget.config(font=large_font)
            elif isinstance(widget, tk.Text):
                widget.config(font=fixed_font)

    def create_single_file_tab(self):
        """创建单个文件计算标签页"""
        self.single_file_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.single_file_tab, text=self.lang.get("single_file_tab"))

        # 文件选择部分
        file_frame = ttk.LabelFrame(self.single_file_tab, text=self.lang.get("select_file"), padding=10)
        file_frame.pack(fill=tk.X, padx=10, pady=5)

        path_frame = ttk.Frame(file_frame)
        path_frame.pack(fill=tk.X, pady=5)

        self.file_path_var = tk.StringVar()
        self.file_path_entry = ttk.Entry(path_frame, textvariable=self.file_path_var, state="readonly")
        self.file_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.browse_button = ttk.Button(path_frame, text=self.lang.get("browse"), command=self.browse_single_file)
        self.browse_button.pack(side=tk.RIGHT)

        # 计算按钮
        self.calculate_button = ttk.Button(
            file_frame,
            text=self.lang.get("calculate_hash"),
            command=self.calculate_single_hash,
            state=tk.DISABLED
        )
        self.calculate_button.pack(pady=10)

        # 结果显示部分
        result_frame = ttk.LabelFrame(self.single_file_tab, text=self.lang.get("result"), padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.result_text = scrolledtext.ScrolledText(
            result_frame,
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        self.result_text.config(font=("楷体", 11))

    def create_compare_files_tab(self):
        """创建文件比较标签页"""
        self.compare_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.compare_tab, text=self.lang.get("compare_files_tab"))

        # 文件1选择部分
        file1_frame = ttk.LabelFrame(self.compare_tab, text=self.lang.get("select_file1"), padding=10)
        file1_frame.pack(fill=tk.X, padx=10, pady=5)

        path1_frame = ttk.Frame(file1_frame)
        path1_frame.pack(fill=tk.X, pady=5)

        self.file1_path_var = tk.StringVar()
        self.file1_path_entry = ttk.Entry(path1_frame, textvariable=self.file1_path_var, state="readonly")
        self.file1_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.browse1_button = ttk.Button(path1_frame, text=self.lang.get("browse"),
                                         command=lambda: self.browse_compare_file(1))
        self.browse1_button.pack(side=tk.RIGHT)

        # 文件2选择部分
        file2_frame = ttk.LabelFrame(self.compare_tab, text=self.lang.get("select_file2"), padding=10)
        file2_frame.pack(fill=tk.X, padx=10, pady=5)

        path2_frame = ttk.Frame(file2_frame)
        path2_frame.pack(fill=tk.X, pady=5)

        self.file2_path_var = tk.StringVar()
        self.file2_path_entry = ttk.Entry(path2_frame, textvariable=self.file2_path_var, state="readonly")
        self.file2_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.browse2_button = ttk.Button(path2_frame, text=self.lang.get("browse"),
                                         command=lambda: self.browse_compare_file(2))
        self.browse2_button.pack(side=tk.RIGHT)

        # 比较按钮
        self.compare_button = ttk.Button(
            self.compare_tab,
            text=self.lang.get("compare_files"),
            command=self.compare_files,
            state=tk.DISABLED
        )
        self.compare_button.pack(pady=10)

        # 比较结果部分
        result_frame = ttk.LabelFrame(self.compare_tab, text=self.lang.get("result"), padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.compare_text = scrolledtext.ScrolledText(
            result_frame,
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.compare_text.pack(fill=tk.BOTH, expand=True)
        self.compare_text.config(font=("楷体", 11))

    def create_folder_hash_tab(self):
        """创建文件夹哈希计算标签页"""
        self.folder_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.folder_tab, text=self.lang.get("folder_hash_tab"))

        # 文件夹选择部分
        folder_frame = ttk.LabelFrame(self.folder_tab, text=self.lang.get("select_folder"), padding=10)
        folder_frame.pack(fill=tk.X, padx=10, pady=5)

        path_frame = ttk.Frame(folder_frame)
        path_frame.pack(fill=tk.X, pady=5)

        self.folder_path_var = tk.StringVar()
        self.folder_path_entry = ttk.Entry(path_frame, textvariable=self.folder_path_var, state="readonly")
        self.folder_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.browse_folder_button = ttk.Button(path_frame, text=self.lang.get("browse"), command=self.browse_folder)
        self.browse_folder_button.pack(side=tk.RIGHT)

        # 计算按钮
        self.calculate_folder_button = ttk.Button(
            folder_frame,
            text=self.lang.get("calculate_folder_hash"),
            command=self.calculate_folder_hash,
            state=tk.DISABLED
        )
        self.calculate_folder_button.pack(pady=10)

        # 进度条
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            folder_frame,
            variable=self.progress_var,
            maximum=100,
            mode="determinate"
        )
        self.progress_bar.pack(fill=tk.X, pady=5)
        self.progress_bar.pack_forget()  # 初始隐藏

        # 结果显示部分
        result_frame = ttk.LabelFrame(self.folder_tab, text=self.lang.get("result"), padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.folder_result_text = scrolledtext.ScrolledText(
            result_frame,
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.folder_result_text.pack(fill=tk.BOTH, expand=True)
        self.folder_result_text.config(font=("楷体", 11))

    def create_folder_compare_tab(self):
        """创建文件夹比较标签页"""
        self.folder_compare_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.folder_compare_tab, text=self.lang.get("folder_compare_tab"))

        # 文件夹1选择部分
        folder1_frame = ttk.LabelFrame(self.folder_compare_tab, text=self.lang.get("select_folder1"), padding=10)
        folder1_frame.pack(fill=tk.X, padx=10, pady=5)

        path1_frame = ttk.Frame(folder1_frame)
        path1_frame.pack(fill=tk.X, pady=5)

        self.folder1_path_var = tk.StringVar()
        self.folder1_path_entry = ttk.Entry(path1_frame, textvariable=self.folder1_path_var, state="readonly")
        self.folder1_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.browse_folder1_button = ttk.Button(path1_frame, text=self.lang.get("browse"),
                                                command=lambda: self.browse_compare_folder(1))
        self.browse_folder1_button.pack(side=tk.RIGHT)

        # 文件夹2选择部分
        folder2_frame = ttk.LabelFrame(self.folder_compare_tab, text=self.lang.get("select_folder2"), padding=10)
        folder2_frame.pack(fill=tk.X, padx=10, pady=5)

        path2_frame = ttk.Frame(folder2_frame)
        path2_frame.pack(fill=tk.X, pady=5)

        self.folder2_path_var = tk.StringVar()
        self.folder2_path_entry = ttk.Entry(path2_frame, textvariable=self.folder2_path_var, state="readonly")
        self.folder2_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.browse_folder2_button = ttk.Button(path2_frame, text=self.lang.get("browse"),
                                                command=lambda: self.browse_compare_folder(2))
        self.browse_folder2_button.pack(side=tk.RIGHT)

        # 比较按钮
        self.compare_folders_button = ttk.Button(
            self.folder_compare_tab,
            text=self.lang.get("compare_files"),
            command=self.compare_folders,
            state=tk.DISABLED
        )
        self.compare_folders_button.pack(pady=10)

        # 进度条
        self.folder_compare_progress_var = tk.DoubleVar()
        self.folder_compare_progress_bar = ttk.Progressbar(
            self.folder_compare_tab,
            variable=self.folder_compare_progress_var,
            maximum=100,
            mode="determinate"
        )
        self.folder_compare_progress_bar.pack(fill=tk.X, padx=10, pady=5)
        self.folder_compare_progress_bar.pack_forget()  # 初始隐藏

        # 比较结果部分
        result_frame = ttk.LabelFrame(self.folder_compare_tab, text=self.lang.get("result"), padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.folder_compare_text = scrolledtext.ScrolledText(
            result_frame,
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.folder_compare_text.pack(fill=tk.BOTH, expand=True)
        self.folder_compare_text.config(font=("楷体", 11))

    def update_status(self, message):
        """更新状态栏消息"""
        self.status_var.set(message)

    def browse_single_file(self):
        """浏览单个文件"""
        file_path = filedialog.askopenfilename(
            title=self.lang.get("select_file"),
            filetypes=[(self.lang.get("all_files"), "*.*")]
        )
        if file_path:
            self.file_path_var.set(file_path)
            self.calculate_button.state(["!disabled"])
            self.update_status(self.lang.get("file_selected", os.path.basename(file_path)))

    def browse_compare_file(self, file_num):
        """浏览比较文件"""
        file_path = filedialog.askopenfilename(
            title=self.lang.get(f"select_file{file_num}"),
            filetypes=[(self.lang.get("all_files"), "*.*")]
        )
        if file_path:
            if file_num == 1:
                self.file1_path_var.set(file_path)
            else:
                self.file2_path_var.set(file_path)

            # 检查两个文件是否都已选择
            if self.file1_path_var.get() and self.file2_path_var.get():
                self.compare_button.state(["!disabled"])

            self.update_status(self.lang.get("file_num_selected", file_num, os.path.basename(file_path)))

    def browse_folder(self):
        """浏览文件夹"""
        folder_path = filedialog.askdirectory(title=self.lang.get("select_folder"))
        if folder_path:
            self.folder_path_var.set(folder_path)
            self.calculate_folder_button.state(["!disabled"])
            self.update_status(self.lang.get("folder_selected", os.path.basename(folder_path)))

    def browse_compare_folder(self, folder_num):
        """浏览比较文件夹"""
        folder_path = filedialog.askdirectory(title=self.lang.get(f"select_folder{folder_num}"))
        if folder_path:
            if folder_num == 1:
                self.folder1_path_var.set(folder_path)
            else:
                self.folder2_path_var.set(folder_path)

            # 检查两个文件夹是否都已选择
            if self.folder1_path_var.get() and self.folder2_path_var.get():
                self.compare_folders_button.state(["!disabled"])

            self.update_status(self.lang.get("folder_num_selected", folder_num, os.path.basename(folder_path)))

    def compute_file_hash(self, file_path):
        """
        计算文件的哈希值

        :param file_path: 文件路径
        :return: (哈希值, 计算耗时) 或 (None, None) 如果出错
        """
        # 检查文件是否存在
        if not os.path.isfile(file_path):
            return None, None

        try:
            algorithm = self.hash_algorithm.get()
            # 初始化哈希对象
            hash_obj = hashlib.new(algorithm)
            file_size = os.path.getsize(file_path)

            # 记录开始时间
            start_time = time.time()

            # 读取文件并计算哈希
            with open(file_path, 'rb') as f:
                while True:
                    data = f.read(65536)  # 64KB块
                    if not data:
                        break
                    hash_obj.update(data)

            # 计算耗时
            elapsed = time.time() - start_time

            return hash_obj.hexdigest(), elapsed
        except Exception as e:
            return None, None

    def compute_folder_hash(self, folder_path, progress_callback=None):
        """
        计算文件夹的哈希值

        :param folder_path: 文件夹路径
        :param progress_callback: 进度回调函数
        :return: (哈希值, 文件数量, 总大小, 计算耗时) 或 (None, 0, 0, 0) 如果出错
        """
        if not os.path.isdir(folder_path):
            return None, 0, 0, 0

        try:
            algorithm = self.hash_algorithm.get()
            hash_obj = hashlib.new(algorithm)
            total_files = 0
            processed_files = 0
            total_size = 0
            start_time = time.time()

            # 首先统计文件总数和总大小
            for root_dir, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root_dir, file)
                    if os.path.isfile(file_path):
                        total_files += 1
                        total_size += os.path.getsize(file_path)

            # 再次遍历文件，计算哈希
            for root_dir, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root_dir, file)
                    if os.path.isfile(file_path):
                        # 添加文件相对路径到哈希
                        rel_path = os.path.relpath(file_path, folder_path)
                        hash_obj.update(rel_path.encode('utf-8'))

                        # 添加文件内容到哈希
                        with open(file_path, 'rb') as f:
                            while True:
                                data = f.read(65536)
                                if not data:
                                    break
                                hash_obj.update(data)

                        processed_files += 1
                        if progress_callback:
                            progress = (processed_files / total_files) * 100
                            progress_callback(progress,
                                              self.lang.get("processing", rel_path, processed_files, total_files))

            # 计算耗时
            elapsed = time.time() - start_time
            return hash_obj.hexdigest(), total_files, total_size, elapsed
        except Exception as e:
            return None, 0, 0, 0

    def calculate_single_hash(self):
        """计算单个文件的哈希值"""
        file_path = self.file_path_var.get()

        if not file_path:
            messagebox.showwarning(self.lang.get("error"), self.lang.get("file_not_selected"))
            return

        if not os.path.isfile(file_path):
            messagebox.showwarning(self.lang.get("error"), self.lang.get("file_not_exist", file_path))
            return

        # 禁用按钮防止重复点击
        self.calculate_button.state(["disabled"])
        self.browse_button.state(["disabled"])
        self.update_status(self.lang.get("calculating_file_hash"))
        self.root.update()  # 立即更新UI

        # 计算哈希值
        hash_value, elapsed = self.compute_file_hash(file_path)

        # 启用按钮
        self.calculate_button.state(["!disabled"])
        self.browse_button.state(["!disabled"])

        if hash_value is None:
            self.update_status(self.lang.get("calculation_failed"))
            messagebox.showerror(self.lang.get("error"), self.lang.get("hash_calculation_error", file_path))
            return

        # 显示结果
        file_size = os.path.getsize(file_path)
        file_size_mb = file_size / (1024 * 1024)  # 转换为MB

        result = self.lang.get("file_path", file_path) + "\n"
        result += self.lang.get("file_size", file_size, file_size_mb) + "\n"
        result += self.lang.get("hash_algorithm", self.hash_algorithm.get().upper()) + "\n"
        result += self.lang.get("time_taken", elapsed) + "\n"
        result += self.lang.get("hash_value", hash_value)

        # 更新结果文本框
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state=tk.DISABLED)

        self.update_status(self.lang.get("calculation_complete", elapsed))

    def compare_files(self):
        """比较两个文件的哈希值"""
        file1 = self.file1_path_var.get()
        file2 = self.file2_path_var.get()

        if not file1 or not file2:
            messagebox.showwarning(self.lang.get("error"), self.lang.get("two_files_required"))
            return

        if not os.path.isfile(file1):
            messagebox.showwarning(self.lang.get("error"), self.lang.get("file_not_exist", file1))
            return

        if not os.path.isfile(file2):
            messagebox.showwarning(self.lang.get("error"), self.lang.get("file_not_exist", file2))
            return

        if os.path.abspath(file1) == os.path.abspath(file2):
            messagebox.showwarning(self.lang.get("error"), self.lang.get("same_file_error"))
            return

        # 禁用按钮防止重复点击
        self.compare_button.state(["disabled"])
        self.browse1_button.state(["disabled"])
        self.browse2_button.state(["disabled"])
        self.update_status(self.lang.get("comparing_files"))
        self.root.update()  # 立即更新UI

        # 计算第一个文件的哈希值
        hash1, elapsed1 = self.compute_file_hash(file1)

        # 计算第二个文件的哈希值
        hash2, elapsed2 = None, None
        if hash1 is not None:
            hash2, elapsed2 = self.compute_file_hash(file2)

        # 启用按钮
        self.compare_button.state(["!disabled"])
        self.browse1_button.state(["!disabled"])
        self.browse2_button.state(["!disabled"])

        if hash1 is None:
            self.update_status(self.lang.get("calculation_failed"))
            messagebox.showerror(self.lang.get("error"), self.lang.get("hash_calculation_error", file1))
            return

        if hash2 is None:
            self.update_status(self.lang.get("calculation_failed"))
            messagebox.showerror(self.lang.get("error"), self.lang.get("hash_calculation_error", file2))
            return

        # 准备比较结果
        result = self.lang.get("file1", file1) + "\n"
        result += self.lang.get("file_size", os.path.getsize(file1)) + "\n"
        result += self.lang.get("file1_hash", self.hash_algorithm.get().upper(), hash1) + "\n"
        result += self.lang.get("time_taken", elapsed1) + "\n\n"

        result += self.lang.get("file2", file2) + "\n"
        result += self.lang.get("file_size", os.path.getsize(file2)) + "\n"
        result += self.lang.get("file2_hash", self.hash_algorithm.get().upper(), hash2) + "\n"
        result += self.lang.get("time_taken", elapsed2) + "\n\n"

        if hash1 == hash2:
            result += self.lang.get("match_success")
        else:
            result += self.lang.get("match_fail")

        # 更新结果文本框
        self.compare_text.config(state=tk.NORMAL)
        self.compare_text.delete(1.0, tk.END)
        self.compare_text.insert(tk.END, result)
        self.compare_text.config(state=tk.DISABLED)

        self.update_status(self.lang.get("comparison_complete", elapsed1 + elapsed2))

    def calculate_folder_hash(self):
        """计算文件夹的哈希值"""
        folder_path = self.folder_path_var.get()

        if not folder_path:
            messagebox.showwarning(self.lang.get("error"), self.lang.get("folder_not_selected"))
            return

        if not os.path.isdir(folder_path):
            messagebox.showwarning(self.lang.get("error"), self.lang.get("folder_not_exist", folder_path))
            return

        # 禁用按钮防止重复点击
        self.calculate_folder_button.state(["disabled"])
        self.browse_folder_button.state(["disabled"])
        self.update_status(self.lang.get("calculating_folder_hash"))

        # 显示进度条
        self.progress_var.set(0)
        self.progress_bar.pack(fill=tk.X, pady=5)
        self.root.update()  # 立即更新UI

        def update_progress(progress, status):
            self.progress_var.set(progress)
            self.update_status(status)
            self.root.update()

        try:
            # 计算文件夹哈希
            folder_hash, total_files, total_size, elapsed = self.compute_folder_hash(
                folder_path,
                update_progress
            )

            if folder_hash is None:
                raise Exception(self.lang.get("folder_hash_error", folder_path))

            # 显示结果
            result = self.lang.get("folder_path", folder_path) + "\n"
            result += self.lang.get("total_files", total_files) + "\n"
            result += self.lang.get("folder_size", total_size, total_size / (1024 * 1024)) + "\n"
            result += self.lang.get("hash_algorithm", self.hash_algorithm.get().upper()) + "\n"
            result += self.lang.get("time_taken", elapsed) + "\n"
            result += self.lang.get("folder_hash", folder_hash)

            # 更新结果文本框
            self.folder_result_text.config(state=tk.NORMAL)
            self.folder_result_text.delete(1.0, tk.END)
            self.folder_result_text.insert(tk.END, result)
            self.folder_result_text.config(state=tk.DISABLED)

            self.update_status(self.lang.get("folder_calculation_complete", elapsed))

        except Exception as e:
            messagebox.showerror(self.lang.get("error"), str(e))
            self.update_status(self.lang.get("folder_calculation_failed"))
        finally:
            # 启用按钮
            self.calculate_folder_button.state(["!disabled"])
            self.browse_folder_button.state(["!disabled"])
            self.progress_bar.pack_forget()  # 隐藏进度条

    def compare_folders(self):
        """比较两个文件夹的哈希值"""
        folder1 = self.folder1_path_var.get()
        folder2 = self.folder2_path_var.get()

        if not folder1 or not folder2:
            messagebox.showwarning(self.lang.get("error"), self.lang.get("two_folders_required"))
            return

        if not os.path.isdir(folder1):
            messagebox.showwarning(self.lang.get("error"), self.lang.get("folder_not_exist", folder1))
            return

        if not os.path.isdir(folder2):
            messagebox.showwarning(self.lang.get("error"), self.lang.get("folder_not_exist", folder2))
            return

        if os.path.abspath(folder1) == os.path.abspath(folder2):
            messagebox.showwarning(self.lang.get("error"), self.lang.get("same_folder_error"))
            return

        # 禁用按钮防止重复点击
        self.compare_folders_button.state(["disabled"])
        self.browse_folder1_button.state(["disabled"])
        self.browse_folder2_button.state(["disabled"])
        self.update_status(self.lang.get("comparing_folders"))

        # 显示进度条
        self.folder_compare_progress_var.set(0)
        self.folder_compare_progress_bar.pack(fill=tk.X, padx=10, pady=5)
        self.root.update()  # 立即更新UI

        def update_progress(progress, status):
            self.folder_compare_progress_var.set(progress)
            self.update_status(status)
            self.root.update()

        try:
            # 计算第一个文件夹的哈希
            self.update_status(self.lang.get("calculating_folder1"))
            hash1, files1, size1, elapsed1 = self.compute_folder_hash(
                folder1,
                lambda p, s: update_progress(p / 2, s)
            )

            if hash1 is None:
                raise Exception(self.lang.get("folder_hash_error", folder1))

            # 计算第二个文件夹的哈希
            self.update_status(self.lang.get("calculating_folder2"))
            hash2, files2, size2, elapsed2 = self.compute_folder_hash(
                folder2,
                lambda p, s: update_progress(50 + p / 2, s)
            )

            if hash2 is None:
                raise Exception(self.lang.get("folder_hash_error", folder2))

            # 准备比较结果
            result = self.lang.get("folder1", folder1) + "\n"
            result += self.lang.get("total_files", files1) + "\n"
            result += self.lang.get("folder_size", size1, size1 / (1024 * 1024)) + "\n"
            result += self.lang.get("hash_algorithm", self.hash_algorithm.get().upper()) + "\n"
            result += self.lang.get("time_taken", elapsed1) + "\n"
            result += self.lang.get("folder1_hash", self.hash_algorithm.get().upper(), hash1) + "\n\n"

            result += self.lang.get("folder2", folder2) + "\n"
            result += self.lang.get("total_files", files2) + "\n"
            result += self.lang.get("folder_size", size2, size2 / (1024 * 1024)) + "\n"
            result += self.lang.get("hash_algorithm", self.hash_algorithm.get().upper()) + "\n"
            result += self.lang.get("time_taken", elapsed2) + "\n"
            result += self.lang.get("folder2_hash", self.hash_algorithm.get().upper(), hash2) + "\n\n"

            if hash1 == hash2:
                result += self.lang.get("folder_match_success")
                if files1 != files2:
                    result += "\n" + self.lang.get("file_count_warning", files1, files2)
                if size1 != size2:
                    result += "\n" + self.lang.get("size_warning", size1 / (1024 * 1024), size2 / (1024 * 1024))
            else:
                result += self.lang.get("folder_match_fail")
                if files1 != files2:
                    result += "\n" + self.lang.get("file_count_different", files1, files2)
                if size1 != size2:
                    result += "\n" + self.lang.get("size_different", size1 / (1024 * 1024), size2 / (1024 * 1024))
                else:
                    result += "\n" + self.lang.get("size_same_content_different")

            # 更新结果文本框
            self.folder_compare_text.config(state=tk.NORMAL)
            self.folder_compare_text.delete(1.0, tk.END)
            self.folder_compare_text.insert(tk.END, result)
            self.folder_compare_text.config(state=tk.DISABLED)

            self.update_status(self.lang.get("folder_comparison_complete", elapsed1 + elapsed2))

        except Exception as e:
            messagebox.showerror(self.lang.get("error"), str(e))
            self.update_status(self.lang.get("comparison_failed"))
        finally:
            # 启用按钮
            self.compare_folders_button.state(["!disabled"])
            self.browse_folder1_button.state(["!disabled"])
            self.browse_folder2_button.state(["!disabled"])
            self.folder_compare_progress_bar.pack_forget()  # 隐藏进度条

    def on_close(self):
        """关闭窗口事件处理"""
        if messagebox.askokcancel(self.lang.get("exit_confirmation"), self.lang.get("exit_message")):
            self.root.destroy()


def main():
    root = tk.Tk()

    # 设置全局字体为楷体，稍大一些
    default_font = ("楷体", 11)
    root.option_add("*Font", default_font)

    app = HashCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()