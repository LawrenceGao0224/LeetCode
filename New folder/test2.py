import win32com.client as win32


# Create Excel and PowerPoint instances
excel_app = win32.Dispatch("Excel.Application")
ppt_app = win32.Dispatch("PowerPoint.Application")


# Open Excel workbook
excel_workbook = excel_app.Workbooks.Open(r'C:\Users\kaosh\Desktop\New folder\Book1.xlsx')
excel_worksheet = excel_workbook.Sheets('Sheet1')  # Adjust the sheet name as needed

# Create PowerPoint presentation
ppt_presentation = ppt_app.Presentations.Open(r"C:\Users\kaosh\Desktop\New folder\power1.pptx")

# Read Excel data and add to PowerPoint slides
for row_index in range(1, excel_worksheet.UsedRange.Rows.Count + 1):
    slide = ppt_presentation.Slides.Add(Index=row_index, Layout=0)  # Layout 1 is Title Slide
    cell_value_A = excel_worksheet.Cells(row_index, 1).Value  # Adjust column index as needed
    cell_value_B = excel_worksheet.Cells(row_index, 2).Value
    cell_value_C = excel_worksheet.Cells(row_index, 3).Value
    cell_value_D = excel_worksheet.Cells(row_index, 4).Value
    #cell_value_E = excel_worksheet.Cells(row_index, 5).Value
    cell_value_F = excel_worksheet.Cells(row_index, 6).Value
    #cell_value_G = excel_worksheet.Cells(row_index, 7).Value


    slide.Shapes[0].TextFrame.TextRange.Text = str(cell_value_B) +" - "+  str(cell_value_C) + "\n" + str(int(cell_value_A))+ ". " + str(cell_value_C)
    slide.Shapes[1].TextFrame.TextRange.Text = str(cell_value_D) 
    slide.Shapes[2].TextFrame.TextRange.Text = str(cell_value_F)
    #slide.Shapes[3].TextFrame.TextRange.Text = str(cell_value_D)
    #slide.Shapes[4].TextFrame.TextRange.Text = str(cell_value_E)
    #slide.Shapes[5].TextFrame.TextRange.Text = str(cell_value_F)
    #slide.Shapes[6].TextFrame.TextRange.Text = str(cell_value_G)

# Save PowerPoint presentation
#ppt_presentation.SaveAs(r'output.pptx')

# Close Excel and PowerPoint instances
excel_workbook.Close()
excel_app.Quit()
#ppt_presentation.Close()
#ppt_app.Quit()