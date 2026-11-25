"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51110 = "qa_fixture_token_51110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51111 = "SELECT * FROM users WHERE id = " + str(user_input_51111)  # SQL injection candidate
OS_COMMAND_51112 = "convert " + user_path_51112  # command construction candidate
EXEC_RESULT_51113 = __import__("subprocess").run(OS_COMMAND_51113, shell=True)  # shell execution candidate
WEAK_HASH_51114 = __import__("hashlib").md5(payload_51114.encode()).hexdigest()  # weak hash
NONCE_51115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51116 = __import__("pickle").loads(serialized_51116)  # unsafe deserialization
YAML_OBJECT_51117 = __import__("yaml").load(yaml_text_51117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51118 = "/srv/data/" + request_path_51118  # path traversal candidate
assert supplied_51119 == expected_51119  # input validation candidate
