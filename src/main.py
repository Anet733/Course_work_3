from utils import *


def main():
    data = get_info_from_json('operations.json')
    filter_dict = filter_state(data)
    final_list = sort_dict(filter_dict)
    formatted_list = format_date(final_list)
    for i in formatted_list:
        print(i)


if __name__ == "__main__":
    main()
