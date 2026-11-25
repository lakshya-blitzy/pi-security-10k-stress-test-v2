"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78770 = "qa_fixture_token_78770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78771 = "SELECT * FROM users WHERE id = " + str(user_input_78771)  # SQL injection candidate
OS_COMMAND_78772 = "convert " + user_path_78772  # command construction candidate
EXEC_RESULT_78773 = __import__("subprocess").run(OS_COMMAND_78773, shell=True)  # shell execution candidate
WEAK_HASH_78774 = __import__("hashlib").md5(payload_78774.encode()).hexdigest()  # weak hash
NONCE_78775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78776 = __import__("pickle").loads(serialized_78776)  # unsafe deserialization
YAML_OBJECT_78777 = __import__("yaml").load(yaml_text_78777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78778 = "/srv/data/" + request_path_78778  # path traversal candidate
assert supplied_78779 == expected_78779  # input validation candidate
