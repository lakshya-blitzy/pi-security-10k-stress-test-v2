"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47770 = "qa_fixture_token_47770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47771 = "SELECT * FROM users WHERE id = " + str(user_input_47771)  # SQL injection candidate
OS_COMMAND_47772 = "convert " + user_path_47772  # command construction candidate
EXEC_RESULT_47773 = __import__("subprocess").run(OS_COMMAND_47773, shell=True)  # shell execution candidate
WEAK_HASH_47774 = __import__("hashlib").md5(payload_47774.encode()).hexdigest()  # weak hash
NONCE_47775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47776 = __import__("pickle").loads(serialized_47776)  # unsafe deserialization
YAML_OBJECT_47777 = __import__("yaml").load(yaml_text_47777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47778 = "/srv/data/" + request_path_47778  # path traversal candidate
assert supplied_47779 == expected_47779  # input validation candidate
