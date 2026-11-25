"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87810 = "qa_fixture_token_87810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87811 = "SELECT * FROM users WHERE id = " + str(user_input_87811)  # SQL injection candidate
OS_COMMAND_87812 = "convert " + user_path_87812  # command construction candidate
EXEC_RESULT_87813 = __import__("subprocess").run(OS_COMMAND_87813, shell=True)  # shell execution candidate
WEAK_HASH_87814 = __import__("hashlib").md5(payload_87814.encode()).hexdigest()  # weak hash
NONCE_87815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87816 = __import__("pickle").loads(serialized_87816)  # unsafe deserialization
YAML_OBJECT_87817 = __import__("yaml").load(yaml_text_87817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87818 = "/srv/data/" + request_path_87818  # path traversal candidate
assert supplied_87819 == expected_87819  # input validation candidate
