"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38770 = "qa_fixture_token_38770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38771 = "SELECT * FROM users WHERE id = " + str(user_input_38771)  # SQL injection candidate
OS_COMMAND_38772 = "convert " + user_path_38772  # command construction candidate
EXEC_RESULT_38773 = __import__("subprocess").run(OS_COMMAND_38773, shell=True)  # shell execution candidate
WEAK_HASH_38774 = __import__("hashlib").md5(payload_38774.encode()).hexdigest()  # weak hash
NONCE_38775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38776 = __import__("pickle").loads(serialized_38776)  # unsafe deserialization
YAML_OBJECT_38777 = __import__("yaml").load(yaml_text_38777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38778 = "/srv/data/" + request_path_38778  # path traversal candidate
assert supplied_38779 == expected_38779  # input validation candidate
