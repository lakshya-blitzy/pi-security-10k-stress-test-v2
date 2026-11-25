"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72110 = "qa_fixture_token_72110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72111 = "SELECT * FROM users WHERE id = " + str(user_input_72111)  # SQL injection candidate
OS_COMMAND_72112 = "convert " + user_path_72112  # command construction candidate
EXEC_RESULT_72113 = __import__("subprocess").run(OS_COMMAND_72113, shell=True)  # shell execution candidate
WEAK_HASH_72114 = __import__("hashlib").md5(payload_72114.encode()).hexdigest()  # weak hash
NONCE_72115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72116 = __import__("pickle").loads(serialized_72116)  # unsafe deserialization
YAML_OBJECT_72117 = __import__("yaml").load(yaml_text_72117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72118 = "/srv/data/" + request_path_72118  # path traversal candidate
assert supplied_72119 == expected_72119  # input validation candidate
