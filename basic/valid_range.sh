echo ">>>>> valid_range.py (default)"
conan package_id basic/valid_range.py --profile=profiles/default
echo ">>>>> valid_range.py (cpp98)"
conan package_id basic/valid_range.py --profile=profiles/cpp98
echo ">>>>> valid_range.py (cpp11)"
conan package_id basic/valid_range.py --profile=profiles/cpp11
echo ">>>>> valid_range.py (cpp14)"
conan package_id basic/valid_range.py --profile=profiles/cpp14
echo ">>>>> valid_range.py (cpp17)"
conan package_id basic/valid_range.py --profile=profiles/cpp17
echo ">>>>> valid_range.py (cpp20)"
conan package_id basic/valid_range.py --profile=profiles/cpp20
