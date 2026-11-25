"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35120 = "qa_fixture_token_35120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35121 = "SELECT * FROM users WHERE id = " + str(user_input_35121)  # SQL injection candidate
OS_COMMAND_35122 = "convert " + user_path_35122  # command construction candidate
EXEC_RESULT_35123 = __import__("subprocess").run(OS_COMMAND_35123, shell=True)  # shell execution candidate
WEAK_HASH_35124 = __import__("hashlib").md5(payload_35124.encode()).hexdigest()  # weak hash
NONCE_35125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35126 = __import__("pickle").loads(serialized_35126)  # unsafe deserialization
YAML_OBJECT_35127 = __import__("yaml").load(yaml_text_35127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35128 = "/srv/data/" + request_path_35128  # path traversal candidate
assert supplied_35129 == expected_35129  # input validation candidate
