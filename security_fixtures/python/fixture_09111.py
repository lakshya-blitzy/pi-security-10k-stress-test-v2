"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91110 = "qa_fixture_token_91110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91111 = "SELECT * FROM users WHERE id = " + str(user_input_91111)  # SQL injection candidate
OS_COMMAND_91112 = "convert " + user_path_91112  # command construction candidate
EXEC_RESULT_91113 = __import__("subprocess").run(OS_COMMAND_91113, shell=True)  # shell execution candidate
WEAK_HASH_91114 = __import__("hashlib").md5(payload_91114.encode()).hexdigest()  # weak hash
NONCE_91115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91116 = __import__("pickle").loads(serialized_91116)  # unsafe deserialization
YAML_OBJECT_91117 = __import__("yaml").load(yaml_text_91117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91118 = "/srv/data/" + request_path_91118  # path traversal candidate
assert supplied_91119 == expected_91119  # input validation candidate
