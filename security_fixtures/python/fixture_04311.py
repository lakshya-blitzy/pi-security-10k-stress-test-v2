"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43110 = "qa_fixture_token_43110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43111 = "SELECT * FROM users WHERE id = " + str(user_input_43111)  # SQL injection candidate
OS_COMMAND_43112 = "convert " + user_path_43112  # command construction candidate
EXEC_RESULT_43113 = __import__("subprocess").run(OS_COMMAND_43113, shell=True)  # shell execution candidate
WEAK_HASH_43114 = __import__("hashlib").md5(payload_43114.encode()).hexdigest()  # weak hash
NONCE_43115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43116 = __import__("pickle").loads(serialized_43116)  # unsafe deserialization
YAML_OBJECT_43117 = __import__("yaml").load(yaml_text_43117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43118 = "/srv/data/" + request_path_43118  # path traversal candidate
assert supplied_43119 == expected_43119  # input validation candidate
