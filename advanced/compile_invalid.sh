echo ">>>>> compile_invalid.py (default)"
conan package_id advanced/compile_invalid.py --profile=profiles/default
echo ">>>>> compile_invalid.py (cpp98)"
conan package_id advanced/compile_invalid.py --profile=profiles/cpp98
echo ">>>>> compile_invalid.py (cpp11)"
conan package_id advanced/compile_invalid.py --profile=profiles/cpp11
echo ">>>>> compile_invalid.py (cpp14)"
conan package_id advanced/compile_invalid.py --profile=profiles/cpp14
echo ">>>>> compile_invalid.py (cpp17)"
conan package_id advanced/compile_invalid.py --profile=profiles/cpp17
echo ">>>>> compile_invalid.py (cpp20)"
conan package_id advanced/compile_invalid.py --profile=profiles/cpp20