"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58110 = "qa_fixture_token_58110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58111 = "SELECT * FROM users WHERE id = " + str(user_input_58111)  # SQL injection candidate
OS_COMMAND_58112 = "convert " + user_path_58112  # command construction candidate
EXEC_RESULT_58113 = __import__("subprocess").run(OS_COMMAND_58113, shell=True)  # shell execution candidate
WEAK_HASH_58114 = __import__("hashlib").md5(payload_58114.encode()).hexdigest()  # weak hash
NONCE_58115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58116 = __import__("pickle").loads(serialized_58116)  # unsafe deserialization
YAML_OBJECT_58117 = __import__("yaml").load(yaml_text_58117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58118 = "/srv/data/" + request_path_58118  # path traversal candidate
assert supplied_58119 == expected_58119  # input validation candidate
