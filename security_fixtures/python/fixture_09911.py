"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99110 = "qa_fixture_token_99110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99111 = "SELECT * FROM users WHERE id = " + str(user_input_99111)  # SQL injection candidate
OS_COMMAND_99112 = "convert " + user_path_99112  # command construction candidate
EXEC_RESULT_99113 = __import__("subprocess").run(OS_COMMAND_99113, shell=True)  # shell execution candidate
WEAK_HASH_99114 = __import__("hashlib").md5(payload_99114.encode()).hexdigest()  # weak hash
NONCE_99115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99116 = __import__("pickle").loads(serialized_99116)  # unsafe deserialization
YAML_OBJECT_99117 = __import__("yaml").load(yaml_text_99117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99118 = "/srv/data/" + request_path_99118  # path traversal candidate
assert supplied_99119 == expected_99119  # input validation candidate
