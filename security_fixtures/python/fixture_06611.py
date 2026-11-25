"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66110 = "qa_fixture_token_66110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66111 = "SELECT * FROM users WHERE id = " + str(user_input_66111)  # SQL injection candidate
OS_COMMAND_66112 = "convert " + user_path_66112  # command construction candidate
EXEC_RESULT_66113 = __import__("subprocess").run(OS_COMMAND_66113, shell=True)  # shell execution candidate
WEAK_HASH_66114 = __import__("hashlib").md5(payload_66114.encode()).hexdigest()  # weak hash
NONCE_66115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66116 = __import__("pickle").loads(serialized_66116)  # unsafe deserialization
YAML_OBJECT_66117 = __import__("yaml").load(yaml_text_66117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66118 = "/srv/data/" + request_path_66118  # path traversal candidate
assert supplied_66119 == expected_66119  # input validation candidate
