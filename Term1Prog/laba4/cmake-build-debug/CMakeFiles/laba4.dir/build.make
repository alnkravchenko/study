# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/alena/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/193.4386.19/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/alena/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/193.4386.19/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/alena/Programming/CPP/laba4

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/alena/Programming/CPP/laba4/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/laba4.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/laba4.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/laba4.dir/flags.make

CMakeFiles/laba4.dir/main.cpp.o: CMakeFiles/laba4.dir/flags.make
CMakeFiles/laba4.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/alena/Programming/CPP/laba4/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/laba4.dir/main.cpp.o"
	/usr/bin/g++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/laba4.dir/main.cpp.o -c /home/alena/Programming/CPP/laba4/main.cpp

CMakeFiles/laba4.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/laba4.dir/main.cpp.i"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/alena/Programming/CPP/laba4/main.cpp > CMakeFiles/laba4.dir/main.cpp.i

CMakeFiles/laba4.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/laba4.dir/main.cpp.s"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/alena/Programming/CPP/laba4/main.cpp -o CMakeFiles/laba4.dir/main.cpp.s

# Object files for target laba4
laba4_OBJECTS = \
"CMakeFiles/laba4.dir/main.cpp.o"

# External object files for target laba4
laba4_EXTERNAL_OBJECTS =

laba4: CMakeFiles/laba4.dir/main.cpp.o
laba4: CMakeFiles/laba4.dir/build.make
laba4: CMakeFiles/laba4.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/alena/Programming/CPP/laba4/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable laba4"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/laba4.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/laba4.dir/build: laba4

.PHONY : CMakeFiles/laba4.dir/build

CMakeFiles/laba4.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/laba4.dir/cmake_clean.cmake
.PHONY : CMakeFiles/laba4.dir/clean

CMakeFiles/laba4.dir/depend:
	cd /home/alena/Programming/CPP/laba4/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/alena/Programming/CPP/laba4 /home/alena/Programming/CPP/laba4 /home/alena/Programming/CPP/laba4/cmake-build-debug /home/alena/Programming/CPP/laba4/cmake-build-debug /home/alena/Programming/CPP/laba4/cmake-build-debug/CMakeFiles/laba4.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/laba4.dir/depend
