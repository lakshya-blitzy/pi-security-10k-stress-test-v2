"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25770 = "qa_fixture_token_25770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25771 = "SELECT * FROM users WHERE id = " + str(user_input_25771)  # SQL injection candidate
OS_COMMAND_25772 = "convert " + user_path_25772  # command construction candidate
EXEC_RESULT_25773 = __import__("subprocess").run(OS_COMMAND_25773, shell=True)  # shell execution candidate
WEAK_HASH_25774 = __import__("hashlib").md5(payload_25774.encode()).hexdigest()  # weak hash
NONCE_25775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25776 = __import__("pickle").loads(serialized_25776)  # unsafe deserialization
YAML_OBJECT_25777 = __import__("yaml").load(yaml_text_25777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25778 = "/srv/data/" + request_path_25778  # path traversal candidate
assert supplied_25779 == expected_25779  # input validation candidate
