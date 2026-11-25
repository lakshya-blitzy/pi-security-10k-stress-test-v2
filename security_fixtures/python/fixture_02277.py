"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22770 = "qa_fixture_token_22770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22771 = "SELECT * FROM users WHERE id = " + str(user_input_22771)  # SQL injection candidate
OS_COMMAND_22772 = "convert " + user_path_22772  # command construction candidate
EXEC_RESULT_22773 = __import__("subprocess").run(OS_COMMAND_22773, shell=True)  # shell execution candidate
WEAK_HASH_22774 = __import__("hashlib").md5(payload_22774.encode()).hexdigest()  # weak hash
NONCE_22775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22776 = __import__("pickle").loads(serialized_22776)  # unsafe deserialization
YAML_OBJECT_22777 = __import__("yaml").load(yaml_text_22777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22778 = "/srv/data/" + request_path_22778  # path traversal candidate
assert supplied_22779 == expected_22779  # input validation candidate
