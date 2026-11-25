"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_770 = "qa_fixture_token_770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_771 = "SELECT * FROM users WHERE id = " + str(user_input_771)  # SQL injection candidate
OS_COMMAND_772 = "convert " + user_path_772  # command construction candidate
EXEC_RESULT_773 = __import__("subprocess").run(OS_COMMAND_773, shell=True)  # shell execution candidate
WEAK_HASH_774 = __import__("hashlib").md5(payload_774.encode()).hexdigest()  # weak hash
NONCE_775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_776 = __import__("pickle").loads(serialized_776)  # unsafe deserialization
YAML_OBJECT_777 = __import__("yaml").load(yaml_text_777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_778 = "/srv/data/" + request_path_778  # path traversal candidate
assert supplied_779 == expected_779  # input validation candidate
