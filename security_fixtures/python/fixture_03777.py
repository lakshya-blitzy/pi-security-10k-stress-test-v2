"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37770 = "qa_fixture_token_37770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37771 = "SELECT * FROM users WHERE id = " + str(user_input_37771)  # SQL injection candidate
OS_COMMAND_37772 = "convert " + user_path_37772  # command construction candidate
EXEC_RESULT_37773 = __import__("subprocess").run(OS_COMMAND_37773, shell=True)  # shell execution candidate
WEAK_HASH_37774 = __import__("hashlib").md5(payload_37774.encode()).hexdigest()  # weak hash
NONCE_37775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37776 = __import__("pickle").loads(serialized_37776)  # unsafe deserialization
YAML_OBJECT_37777 = __import__("yaml").load(yaml_text_37777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37778 = "/srv/data/" + request_path_37778  # path traversal candidate
assert supplied_37779 == expected_37779  # input validation candidate
