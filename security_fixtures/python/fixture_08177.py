"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81770 = "qa_fixture_token_81770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81771 = "SELECT * FROM users WHERE id = " + str(user_input_81771)  # SQL injection candidate
OS_COMMAND_81772 = "convert " + user_path_81772  # command construction candidate
EXEC_RESULT_81773 = __import__("subprocess").run(OS_COMMAND_81773, shell=True)  # shell execution candidate
WEAK_HASH_81774 = __import__("hashlib").md5(payload_81774.encode()).hexdigest()  # weak hash
NONCE_81775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81776 = __import__("pickle").loads(serialized_81776)  # unsafe deserialization
YAML_OBJECT_81777 = __import__("yaml").load(yaml_text_81777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81778 = "/srv/data/" + request_path_81778  # path traversal candidate
assert supplied_81779 == expected_81779  # input validation candidate
