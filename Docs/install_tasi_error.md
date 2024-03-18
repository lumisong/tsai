# 安装 tsai

## 前提

1. 新的虚拟环境 python3.8,cuda11.8

## 安装方式

最终选择 pip 安装，conda安装会存在很多问题

## conda 安装问题

前提：为什么选择pip安装，而不是conda安装？tsai包的conda安装命令`conda install -c timeseriesai tsai`，但是

使用conda问题：

1. 确定出现的问题：
   1. 网络问题，conda安装速度慢，或者直接无法安装
   2. 源问题：conda默认源，conda-forge源，timeseriesai源,镜像源的选择问题。
2. 可能出现的问题：
   1. conda安装的tsai包版本可能较低，不支持最新的功能(官方的更新发布情况)。

## 安装疑问

1. 由于网络隔离，本地机器需要开启代理才能访问部分包管理的源地址，在终端，conda没有配置代码，但是在我网页浏览上是成功配置了代理的。现在我想去寻找镜像源，本机能访问到的镜像站，去对于镜像站是否有同步我所需要的包。
2. 使用的是timeseries的channel，不是默认channel，也不是conda-forge.不明白这些channel的区别。
3. 镜像站去比对，是否镜像站中是否有更新所需要的package。如果想在使用镜像站的情况下去安装tsai

### channel概念

如何在特定的镜像站中查找并安装特定的包。

`Channel`是存储包的位置，相当于一个包的仓库。Conda通过这些Channels来下载和更新包。默认情况下，Conda会从默认channel下载包，但用户可以指定其他的channel来下载，例如conda-forge。

- `conda-forge`是一个社区驱动的channel，提供了大量的包，其作用类似于PyPI，但拥有统一的自动构建基础设施，并且进行了更多的同行评审。
- `-c timeseries`指定了Conda应该从`timeseries`这个`channel`中搜索并安装tsai包。这意味着`timeseries`是除默认`channel`和`conda-forge`之外的另一个包源。

### 使用镜像源安装包

镜像站，如清华大学镜像站，同步官方Conda仓库内容。镜像站中查找并安装tsai包，需要进行以下操作：

1. 更换Conda源：首将Conda的包源更换为能够访问的镜像站。修改.condarc文件来实现，文件位于用户的主目录。可以通过以下命令添加清华大学镜像源为例：

    ```bash
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
    ```

    ```bash
    conda config --set show_channel_urls yes
    ```

    其他镜像源，只需将URL替换为相应的镜像地址。
2. 搜索包：配置镜像源后，使用conda search命令来搜索tsai包，以确认该镜像站是否有需要的包及其版本。例如：

    ```bash
    conda search tsai --channel <镜像站的channel>
    ```

    如果不确定镜像站的具体channel名称，可以先尝试不加--channel选项进行搜索。

3. 安装包：确认镜像站中有需要的tsai包，可以通过以下命令进行安装：

    ```bash
    conda install tsai -c <镜像站的channel>
    ```

    已经将镜像站配置为Conda的默认搜索channel，那么在安装时可能不需要再指定-c选项。

**注意事项**:
    由于网络隔离和代理的问题，确保在执行上述操作之前，代理设置已经正确配置，以便Conda可以通过代理访问网络。
    如果网络环境极其特殊，导致即使是镜像站也无法访问，那么可能需要考虑使用其他方式来手动下载并安装包，或者寻求网络环境的调整。

### 镜像源对比包

网页直接检查和比较源地址与能访问的镜像站中的包，可以按照以下步骤操作：

1. 访问官方Conda仓库或特定channel的网页
    尝试访问官方Conda仓库或想要安装的包所在的特定channel（例如timeseries）。可能需要一些搜索，因为不是所有的channel都有易于浏览的网页界面。对于conda-forge，您可以直接访问其在GitHub上的页面，或者其在Anaconda.org上的页面来浏览包。
2. 访问可以访问的镜像站
    如清华大学镜像站（<https://mirrors.tuna.tsinghua.edu.cn/> 或网易镜像站<https://mirrors.163.com/>。这些镜像站通常会有搜索功能，搜索特定的包。例如，在清华大学镜像站，您可以通过其提供的搜索框来搜索tsai包。
3. 比对包的存在和版本
    镜像站的搜索结果中，检查tsai包是否存在，以及其可用的版本。可以通过比较官方仓库或特定channel与镜像站中的信息来确定需要的版本是否可用。
4. 直接下载包（可选）
    所需的包和版本，而且镜像站提供了直接下载的链接，可以选择手动下载包到本地机器。下载后，可以使用conda命令来安装下载的包，使用如下命令：

    ```bash
    conda install /path/to/downloaded/package
    ```

    假定已经下载包并知道其在本地文件系统中的位置。

**注意事项:**

 1. 手动下载和安装包的方法虽然可以绕过一些网络问题，但也可能会错过自动解决依赖关系的便利。因此，这种方法更适合于那些无法通过正常途径安装包的情况。
 2. 在下载和安装之前，请确保所下载的包版本与您的项目依赖相兼容。

通过上述方法，可以在网页上手动检查和下载所需的包，从而绕过一些网络和代理设置的限制。
