"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76110 = "qa_fixture_token_76110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76111 = "SELECT * FROM users WHERE id = " + str(user_input_76111)  # SQL injection candidate
OS_COMMAND_76112 = "convert " + user_path_76112  # command construction candidate
EXEC_RESULT_76113 = __import__("subprocess").run(OS_COMMAND_76113, shell=True)  # shell execution candidate
WEAK_HASH_76114 = __import__("hashlib").md5(payload_76114.encode()).hexdigest()  # weak hash
NONCE_76115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76116 = __import__("pickle").loads(serialized_76116)  # unsafe deserialization
YAML_OBJECT_76117 = __import__("yaml").load(yaml_text_76117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76118 = "/srv/data/" + request_path_76118  # path traversal candidate
assert supplied_76119 == expected_76119  # input validation candidate
