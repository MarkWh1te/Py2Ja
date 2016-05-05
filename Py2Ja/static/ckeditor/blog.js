CKEDITOR.editorConfig = function( config ) {
	// The toolbar groups arrangement, optimized for two toolbar rows.
	config.toolbarGroups = [
		{ name: 'clipboard',   groups: [ 'clipboard', 'undo' ] },
		{ name: 'editing',     groups: [ 'find', 'selection', 'spellchecker' ] },
		{ name: 'links' },
		{ name: 'insert' },
		{ name: 'forms' },
		{ name: 'document',	   groups: [ 'mode', 'document', 'doctools' ] },
		'/',
		{ name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
		{ name: 'paragraph',   groups: [ 'list', 'indent', 'blocks', 'align', 'bidi' ] },
		{ name: 'styles' },
		{ name: 'colors' },
	];

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
	    c: 'C',
        cpp: 'C++',
        java: 'Java',
        php: 'PHP',
        python: 'Python',
        html: 'HTML',
        css: 'CSS',
        javascript: 'JavaScript',
        json: 'JSON',
        sql: 'SQL',
    };

    config.height = 400;

    config.resize_enabled = false;

    config.skin = 'minimalist';

    config.image_previewText=' ';
    config.filebrowserImageUploadUrl= "/blog/write/image-upload/";
};
