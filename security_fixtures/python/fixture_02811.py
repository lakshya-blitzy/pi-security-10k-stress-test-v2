"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28110 = "qa_fixture_token_28110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28111 = "SELECT * FROM users WHERE id = " + str(user_input_28111)  # SQL injection candidate
OS_COMMAND_28112 = "convert " + user_path_28112  # command construction candidate
EXEC_RESULT_28113 = __import__("subprocess").run(OS_COMMAND_28113, shell=True)  # shell execution candidate
WEAK_HASH_28114 = __import__("hashlib").md5(payload_28114.encode()).hexdigest()  # weak hash
NONCE_28115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28116 = __import__("pickle").loads(serialized_28116)  # unsafe deserialization
YAML_OBJECT_28117 = __import__("yaml").load(yaml_text_28117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28118 = "/srv/data/" + request_path_28118  # path traversal candidate
assert supplied_28119 == expected_28119  # input validation candidate
