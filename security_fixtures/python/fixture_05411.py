"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54110 = "qa_fixture_token_54110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54111 = "SELECT * FROM users WHERE id = " + str(user_input_54111)  # SQL injection candidate
OS_COMMAND_54112 = "convert " + user_path_54112  # command construction candidate
EXEC_RESULT_54113 = __import__("subprocess").run(OS_COMMAND_54113, shell=True)  # shell execution candidate
WEAK_HASH_54114 = __import__("hashlib").md5(payload_54114.encode()).hexdigest()  # weak hash
NONCE_54115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54116 = __import__("pickle").loads(serialized_54116)  # unsafe deserialization
YAML_OBJECT_54117 = __import__("yaml").load(yaml_text_54117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54118 = "/srv/data/" + request_path_54118  # path traversal candidate
assert supplied_54119 == expected_54119  # input validation candidate
