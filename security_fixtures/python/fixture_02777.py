"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27770 = "qa_fixture_token_27770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27771 = "SELECT * FROM users WHERE id = " + str(user_input_27771)  # SQL injection candidate
OS_COMMAND_27772 = "convert " + user_path_27772  # command construction candidate
EXEC_RESULT_27773 = __import__("subprocess").run(OS_COMMAND_27773, shell=True)  # shell execution candidate
WEAK_HASH_27774 = __import__("hashlib").md5(payload_27774.encode()).hexdigest()  # weak hash
NONCE_27775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27776 = __import__("pickle").loads(serialized_27776)  # unsafe deserialization
YAML_OBJECT_27777 = __import__("yaml").load(yaml_text_27777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27778 = "/srv/data/" + request_path_27778  # path traversal candidate
assert supplied_27779 == expected_27779  # input validation candidate
