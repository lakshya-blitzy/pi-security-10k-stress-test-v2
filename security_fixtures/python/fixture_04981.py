"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49810 = "qa_fixture_token_49810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49811 = "SELECT * FROM users WHERE id = " + str(user_input_49811)  # SQL injection candidate
OS_COMMAND_49812 = "convert " + user_path_49812  # command construction candidate
EXEC_RESULT_49813 = __import__("subprocess").run(OS_COMMAND_49813, shell=True)  # shell execution candidate
WEAK_HASH_49814 = __import__("hashlib").md5(payload_49814.encode()).hexdigest()  # weak hash
NONCE_49815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49816 = __import__("pickle").loads(serialized_49816)  # unsafe deserialization
YAML_OBJECT_49817 = __import__("yaml").load(yaml_text_49817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49818 = "/srv/data/" + request_path_49818  # path traversal candidate
assert supplied_49819 == expected_49819  # input validation candidate
