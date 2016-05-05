CKEDITOR.editorConfig = function( config ) {
	// The toolbar groups arrangement, optimized for two toolbar rows.

	// Remove some buttons provided by the standard plugins, which are
	// not needed in the Standard(s) toolbar.
    config.removeButtons = 'Underline,Subscript,Superscript';

	// Set the most common block elements.
	config.format_tags = 'p;h1;h2;h3;pre';

	// Simplify the dialog windows.
	config.removeDialogTabs = 'image:advanced;link:advanced';


    // my settings
	config.extraPlugins = 'codesnippet';

	config.codeSnippet_theme = 'zenburn';

	config.codeSnippet_languages = {
        cpp: 'C++',
        html: 'HTML',
        java: 'Java',
        javascript: 'JavaScript',
        json: 'JSON',
        php: 'PHP',
        python: 'Python',
        sql: 'SQL',
    };

    config.height = 400;

    config.resize_enabled = false;

    config.skin = 'minimalist';

    config.fontSize_defaultLabel = '28px';
};
