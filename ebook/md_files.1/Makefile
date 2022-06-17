CHAPTERS = Chapter_00_-_Preface/00_Preface.md  Chapter_01_-_Introduction/01_Introduction.md  Chapter_02_-_Basics/2.0.0_Starting_Point.md  Chapter_02_-_Basics/2.0.1_Python_Installation.md Chapter_02_-_Basics/2.1._Syntax.md  Chapter_02_-_Basics/2.2._Python_Identifiers.md Chapter_02_-_Basics/2.3._Maths_Operators.md  Chapter_02_-_Basics/2.4_Code_Introspection.md  Chapter_02_-_Basics/2.6_Python_Naming_Conventions.md  Chapter_02_-_Basics/Mutables_and_Immutables.md  Chapter_02_-_Basics/2.3.1_Exercises_-_Maths_Operations.md  Chapter_02_-_Basics/2.5_Python_in-built_Documentation.md  Chapter_03_-_Control_Flow/3.1%20Compound%20Statements.md Chapter_03_-_Control_Flow/3.1%20Exercises%20-%20Conditions.md  Chapter_04_-_Loops/Chapter%204%20-%20Loops.md  Chapter_05_-_Data_Types/5.0_Data_Types.md  Chapter_05_-_Data_Types/5.0.1_Answers_-_Data_Type.md  Chapter_05_-_Data_Types/5.1.1_Questions_-_Dictionary.md  Chapter_06_-_Functions/6.0_Functions.md  Chapter_06_-_Functions/6.1_Lamda.md  Chapter_06_-_Functions/6.2_Excersise_-_Function.md  Chapter_07_-_Scope/Scope_of_names.md Chapter_08_-_Modules/Chapter8_Modules.md  Chapter_09_-_Classes_and_OOPS/1.0_Classes_and_OOPS.md  Chapter_09_-_Classes_and_OOPS/2.0._OOPs_Fundamentals_-_Inheritance.md  Chapter_09_-_Classes_and_OOPS/2.2_Multiple_Inheritance.md Chapter_09_-_Classes_and_OOPS/2.1_Single_Inheritance.md  Chapter_09_-_Classes_and_OOPS/3._OOPs_Fundamentals_-_Polymorphism.md  Chapter_09_-_Classes_and_OOPS/4._OOPs_Fundamentals_-_Composition.md  Chapter_09_-_Classes_and_OOPS/5._OOPs_Fundamentals_-_Inner_Class.md  Chapter_09_-_Classes_and_OOPS/6._OOPs_Fundamentals_-_ABC.md  Chapter_09_-_Classes_and_OOPS/7._MetaProgramming.md  Chapter_10_-_Generators/Generators.md  Chapter_11_-_Exceptions/Exceptions.md  Chapter_12_-_Introspection/Introspection.md  Chapter_13_-_Decorators/Decorators.md  Chapter_14_-_Properties/property.md  Chapter_16_-_Standard_library/print.md  Chapter_16_-_Standard_library/Standard_library.md  Chapter_17_-Third_Party_Libraries/Third_Party_Libraries.md  Chapter_18_-_Reference,_Shallow_and_deep_copy/Reference,_Shallow_and_deep_copy.md   


EPUB_FILE = build/book.epub
MOBI_FILE = build/book.mobi
PDF_FILE = build/book.pdf


.PHONY: all
all: $(EPUB_FILE) $(MOBI_FILE) $(PDF_FILE)

.PHONY: clean
clean:
	rm -f build/*

.PHONY: epub
epub: $(EPUB_FILE)

.PHONY: mobi
mobi: $(MOBI_FILE)

.PHONY: pdf
pdf: $(PDF_FILE)


.PHONY: preview
preview: $(MOBI_FILE)
	ebook-viewer $(MOBI_FILE)


$(EPUB_FILE): clean $(CHAPTERS) meta/title.txt meta/cover.png meta/stylesheet.css meta/metadata.xml
	pandoc \
		-o $(EPUB_FILE) \
		meta/title.txt \
		$(CHAPTERS) \
		--epub-cover-image=meta/cover.jpg \
		--css=meta/stylesheet.css \
		--epub-metadata=meta/metadata.xml \
		--table-of-contents

$(PDF_FILE): $(CHAPTERS) meta/title.txt
	pandoc \
		-o $(PDF_FILE) \
		meta/title.txt \
		$(CHAPTERS) \
		--toc
