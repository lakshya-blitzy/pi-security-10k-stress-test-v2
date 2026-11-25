"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87110 = "qa_fixture_token_87110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87111 = "SELECT * FROM users WHERE id = " + str(user_input_87111)  # SQL injection candidate
OS_COMMAND_87112 = "convert " + user_path_87112  # command construction candidate
EXEC_RESULT_87113 = __import__("subprocess").run(OS_COMMAND_87113, shell=True)  # shell execution candidate
WEAK_HASH_87114 = __import__("hashlib").md5(payload_87114.encode()).hexdigest()  # weak hash
NONCE_87115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87116 = __import__("pickle").loads(serialized_87116)  # unsafe deserialization
YAML_OBJECT_87117 = __import__("yaml").load(yaml_text_87117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87118 = "/srv/data/" + request_path_87118  # path traversal candidate
assert supplied_87119 == expected_87119  # input validation candidate
