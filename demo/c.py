import time
import textwrap
from colorama import Fore, Style, init

# Khởi tạo colorama
init(autoreset=True)

def display_lines_with_color(lines, delay=2, wrap_width=80):
    """
    Hiển thị từng đoạn văn bản với màu sắc và khoảng thời gian chờ giữa các đoạn.

    Args:
        lines (list): Danh sách các đoạn văn bản cần hiển thị.
        delay (int): Thời gian chờ giữa mỗi đoạn (tính bằng giây).
        wrap_width (int): Chiều rộng dòng để tự động xuống dòng.
    """
    # Danh sách các màu
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

    for i, line in enumerate(lines):
        color = colors[i % len(colors)]  # Chọn màu theo vòng lặp
        wrapped_lines = textwrap.wrap(line, width=wrap_width)  # Tự động xuống dòng
        for wrapped_line in wrapped_lines:
            print(color + wrapped_line)  # In dòng với màu sắc
        time.sleep(delay)
        print()  # Dòng trống để tách biệt các đoạn

# Danh sách văn bản cần hiển thị
text_lines = [
    "Phần I. Đọc hiểu (6,0 điểm)",

    "Câu 1: Bài thơ được viết theo thể thơ nào?  \nBài thơ được viết theo thể thất ngôn bát cú đường luật.",

    "Câu 2: Chỉ ra sự phá cách về vần của tác giả trong bài thơ?  \nTrong bài thơ, vần thơ không được tuân thủ hoàn toàn theo luật niêm luật của thơ thất ngôn bát cú:  \n- Vần \"thua\" ở câu 1 và \"mùa\" ở câu 2 không hoàn toàn hài hòa với vần \"bò\" ở câu 4.  \n- Tác giả sử dụng cách ngắt vần sáng tạo, phù hợp với nội dung giản dị, đời thường.",

    "Câu 3: Xác định nhân vật trữ tình trong bài thơ.  \nNhân vật trữ tình trong bài thơ là một người nông dân nghèo ở nông thôn, đại diện cho tầng lớp lao động cực khổ thời phong kiến thuộc địa.",

    "Câu 4: Phân tích hiệu quả nghệ thuật của biện pháp tu từ liệt kê trong hai câu thơ sau:  \nPhần thuế quan Tây, phần trả nợ  \nNửa công đứa ở, nửa thuê bò  \n- Biện pháp tu từ liệt kê nhấn mạnh nỗi khổ cực, thiếu thốn của người nông dân: họ phải gánh nhiều khoản chi tiêu như thuế quan, trả nợ, thuê lao động, thuê bò.  \n- Những cụm từ \"phần thuế\", \"phần trả nợ\", \"nửa công\", \"nửa thuê\" tạo cảm giác chồng chất khó khăn, thể hiện sự kiệt quệ về tài chính và sức lực.  \n- Qua đó, tác giả làm nổi bật sự bất công của xã hội đương thời.",

    "Câu 5: Nội dung khái quát của bài thơ là gì?  \nBài thơ khắc họa bức tranh chân thực, đau thương về cuộc sống nghèo đói, cực nhọc của người nông dân trong xã hội phong kiến thực dân, đồng thời bộc lộ niềm cảm thông sâu sắc của tác giả đối với họ.",

    "Câu 6: Anh/chị hiểu như thế nào về hai câu thơ cuối?  \nTằn tiện thế mà không khá nhỉ?  \nNhờ trời rồi cũng mấy gian kho.  \n- Hai câu thơ thể hiện sự chua xót và mỉa mai trước thực trạng: dù đã cố gắng tằn tiện, làm lụng chăm chỉ, người nông dân vẫn không thoát khỏi cảnh nghèo khó.  \n- Câu thơ cuối nói về sự phó mặc cho số phận, một niềm tin vào sự đổi thay nhưng đầy bi quan.",

    "Câu 7: Bài thơ gợi cho anh/chị suy nghĩ gì về cách ứng xử trước những khó khăn trong cuộc sống?  \n- Bài thơ cho thấy trước khó khăn, con người cần biết chấp nhận và kiên nhẫn vượt qua.  \n- Tuy nhiên, thay vì phó mặc hoàn toàn cho số phận, cần có ý chí phấn đấu và tìm cách thay đổi hoàn cảnh.",

    "Câu 8: Nhận xét về vẻ đẹp tâm hồn của nhà thơ Nguyễn Khuyến (trong đoạn văn 7-10 dòng).  \nNguyễn Khuyến là một nhà thơ với tấm lòng nhân ái sâu sắc. Qua bài thơ \"Chốn quê,\" ông thể hiện sự thấu hiểu, đồng cảm chân thành với nỗi khổ cực của người nông dân. Ông không chỉ cảm thông mà còn phê phán bất công xã hội bằng giọng thơ mộc mạc, bình dị nhưng thấm thía. Vẻ đẹp tâm hồn của ông là sự gần gũi, tình yêu thương với nhân dân và quê hương, dù bản thân là người trí thức trong xã hội phong kiến. Chính điều này làm thơ ông không chỉ giàu giá trị nhân văn mà còn luôn sống mãi trong lòng người đọc.",

    "Phần II. Viết (4,0 điểm)",

    "Đề bài: Từ nội dung văn bản ở phần Đọc hiểu, hãy viết bài văn trình bày suy nghĩ của anh/chị về vai trò của tình yêu quê hương, đất nước đối với thế hệ trẻ hiện nay.",

    "Bài viết tham khảo:  \nTình yêu quê hương, đất nước luôn là nguồn cảm hứng vĩ đại và là giá trị cốt lõi gắn bó dân tộc Việt Nam qua nhiều thế hệ. Đối với thế hệ trẻ ngày nay, tình yêu quê hương không chỉ là lòng tự hào về truyền thống dân tộc mà còn đóng vai trò quan trọng trong việc thúc đẩy sự phát triển của xã hội.  \nTình yêu quê hương khơi dậy tinh thần trách nhiệm với cộng đồng và đất nước. Thế hệ trẻ cần nhận thức rằng mỗi hành động nhỏ, như học tập, lao động hay bảo vệ môi trường, đều góp phần xây dựng quê hương thêm giàu đẹp. Ngoài ra, tình yêu đất nước cũng là động lực để thanh niên không ngừng đổi mới, sáng tạo, nâng cao tri thức, từ đó đưa Việt Nam sánh vai với các cường quốc năm châu.  \nTrong bối cảnh hội nhập toàn cầu, tình yêu quê hương còn là ý thức giữ gìn bản sắc văn hóa dân tộc. Mỗi người trẻ cần ý thức rằng việc bảo tồn giá trị truyền thống chính là cách thể hiện lòng yêu nước sâu sắc. Đồng thời, tình yêu quê hương cũng giúp thế hệ trẻ đoàn kết, vững vàng trước mọi thử thách, khó khăn trong cuộc sống.  \nTóm lại, tình yêu quê hương, đất nước là nguồn sức mạnh tinh thần to lớn. Nó định hướng thế hệ trẻ hành động vì tương lai của dân tộc và tạo nên một đất nước giàu đẹp, văn minh."
]

# Gọi hàm để hiển thị từng đoạn văn bản với thời gian chờ 3 giây và màu sắc
display_lines_with_color(text_lines, delay=3)
