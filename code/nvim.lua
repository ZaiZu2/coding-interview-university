return {
	neotest_python = {
		is_test_file = function(file_path)
			local file_suffix = string.sub(file_path, #file_path - 2, #file_path)
			if file_suffix == ".py" then
				return true
			else
				return false
			end
		end,
	},
}
