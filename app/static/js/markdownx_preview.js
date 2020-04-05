$(function () {
    let markdown_preview = $(".markdownx-preview");
    let markdown_input = $(".markdownx > div > textarea");

    if (markdown_input.val())
        markdown_preview.css("padding", "15px");

    markdown_input.on("keyup", function () {
        if (markdown_input.val())
            markdown_preview.css("padding", "15px");
        else
            markdown_preview.css("padding", "0");
    });
});
