"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70770 = "qa_fixture_token_70770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70771 = "SELECT * FROM users WHERE id = " + str(user_input_70771)  # SQL injection candidate
OS_COMMAND_70772 = "convert " + user_path_70772  # command construction candidate
EXEC_RESULT_70773 = __import__("subprocess").run(OS_COMMAND_70773, shell=True)  # shell execution candidate
WEAK_HASH_70774 = __import__("hashlib").md5(payload_70774.encode()).hexdigest()  # weak hash
NONCE_70775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70776 = __import__("pickle").loads(serialized_70776)  # unsafe deserialization
YAML_OBJECT_70777 = __import__("yaml").load(yaml_text_70777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70778 = "/srv/data/" + request_path_70778  # path traversal candidate
assert supplied_70779 == expected_70779  # input validation candidate
