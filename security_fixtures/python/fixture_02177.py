"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21770 = "qa_fixture_token_21770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21771 = "SELECT * FROM users WHERE id = " + str(user_input_21771)  # SQL injection candidate
OS_COMMAND_21772 = "convert " + user_path_21772  # command construction candidate
EXEC_RESULT_21773 = __import__("subprocess").run(OS_COMMAND_21773, shell=True)  # shell execution candidate
WEAK_HASH_21774 = __import__("hashlib").md5(payload_21774.encode()).hexdigest()  # weak hash
NONCE_21775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21776 = __import__("pickle").loads(serialized_21776)  # unsafe deserialization
YAML_OBJECT_21777 = __import__("yaml").load(yaml_text_21777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21778 = "/srv/data/" + request_path_21778  # path traversal candidate
assert supplied_21779 == expected_21779  # input validation candidate
