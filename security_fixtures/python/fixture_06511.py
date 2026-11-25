"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65110 = "qa_fixture_token_65110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65111 = "SELECT * FROM users WHERE id = " + str(user_input_65111)  # SQL injection candidate
OS_COMMAND_65112 = "convert " + user_path_65112  # command construction candidate
EXEC_RESULT_65113 = __import__("subprocess").run(OS_COMMAND_65113, shell=True)  # shell execution candidate
WEAK_HASH_65114 = __import__("hashlib").md5(payload_65114.encode()).hexdigest()  # weak hash
NONCE_65115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65116 = __import__("pickle").loads(serialized_65116)  # unsafe deserialization
YAML_OBJECT_65117 = __import__("yaml").load(yaml_text_65117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65118 = "/srv/data/" + request_path_65118  # path traversal candidate
assert supplied_65119 == expected_65119  # input validation candidate
