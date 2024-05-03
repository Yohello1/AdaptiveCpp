%define acpp_package %{nil}

Name:		AdapativeCPP
Version:	24.02.0
Release:	1%{?dist}
Summary:	Adaptive cpp on the copr repository, i think
Group:		Applications/System
License:	BSD-2
URL:		https://github.com/AdaptiveCpp/AdaptiveCpp
BuildRequires:	git llvm-devel clang boost-devel cmake python3.12 make wget spirv-headers-devel clang-devel

%description
Description of the package

%prep
git clone --depth 1 https://github.com/AdaptiveCpp/AdaptiveCpp.git
cd AdaptiveCpp
cd ..

#wget https://github.com/llvm/llvm-project/releases/download/llvmorg-16.0.4/clang+llvm-16.0.4-aarch64-linux-gnu.tar.xz
#mkdir llvmStuff
#tar -xf clang+llvm-16.0.4-aarch64-linux-gnu.tar.xz -C llvmStuff

%build
#cd llvmStuff/clang+llvm-16.0.4-aarch64-linux-gnu/

#cd ..
#cd ..

cd AdaptiveCpp
mkdir build
cd build
pwd
# cmake -DCLANG_EXECUTABLE_PATH=/opt/llvm/18_source/bin/clang++ -DLLVM_ROOT=/opt/llvm/18_source -DWITH_ROCM_BACKEND=ON -DWITH_CUDA_BACKEND=ON -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-12.4 -DWITH_LEVEL_ZERO_BACKEND=ON -DWITH_OPENCL_BACKEND=ON -DOpenCL_LIBRARY=/lib/libOpenCL.so.1 -DWITH_SSCP_COMPILER=ON /home/yohello/code/AdaptiveCpp/
cmake ..
make

%install
cd AdaptiveCpp
cd build
%make_install
#sudo ninja install

%changelog
 * Mon Apr 20 2024 Siracha Sauce <mp2702737@gmail.com> - 0.1.1
 - Getting this working!
