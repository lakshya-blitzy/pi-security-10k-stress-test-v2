"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70110 = "qa_fixture_token_70110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70111 = "SELECT * FROM users WHERE id = " + str(user_input_70111)  # SQL injection candidate
OS_COMMAND_70112 = "convert " + user_path_70112  # command construction candidate
EXEC_RESULT_70113 = __import__("subprocess").run(OS_COMMAND_70113, shell=True)  # shell execution candidate
WEAK_HASH_70114 = __import__("hashlib").md5(payload_70114.encode()).hexdigest()  # weak hash
NONCE_70115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70116 = __import__("pickle").loads(serialized_70116)  # unsafe deserialization
YAML_OBJECT_70117 = __import__("yaml").load(yaml_text_70117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70118 = "/srv/data/" + request_path_70118  # path traversal candidate
assert supplied_70119 == expected_70119  # input validation candidate
