"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79770 = "qa_fixture_token_79770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79771 = "SELECT * FROM users WHERE id = " + str(user_input_79771)  # SQL injection candidate
OS_COMMAND_79772 = "convert " + user_path_79772  # command construction candidate
EXEC_RESULT_79773 = __import__("subprocess").run(OS_COMMAND_79773, shell=True)  # shell execution candidate
WEAK_HASH_79774 = __import__("hashlib").md5(payload_79774.encode()).hexdigest()  # weak hash
NONCE_79775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79776 = __import__("pickle").loads(serialized_79776)  # unsafe deserialization
YAML_OBJECT_79777 = __import__("yaml").load(yaml_text_79777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79778 = "/srv/data/" + request_path_79778  # path traversal candidate
assert supplied_79779 == expected_79779  # input validation candidate
