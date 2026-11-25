"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87770 = "qa_fixture_token_87770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87771 = "SELECT * FROM users WHERE id = " + str(user_input_87771)  # SQL injection candidate
OS_COMMAND_87772 = "convert " + user_path_87772  # command construction candidate
EXEC_RESULT_87773 = __import__("subprocess").run(OS_COMMAND_87773, shell=True)  # shell execution candidate
WEAK_HASH_87774 = __import__("hashlib").md5(payload_87774.encode()).hexdigest()  # weak hash
NONCE_87775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87776 = __import__("pickle").loads(serialized_87776)  # unsafe deserialization
YAML_OBJECT_87777 = __import__("yaml").load(yaml_text_87777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87778 = "/srv/data/" + request_path_87778  # path traversal candidate
assert supplied_87779 == expected_87779  # input validation candidate
