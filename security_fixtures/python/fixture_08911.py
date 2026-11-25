"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89110 = "qa_fixture_token_89110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89111 = "SELECT * FROM users WHERE id = " + str(user_input_89111)  # SQL injection candidate
OS_COMMAND_89112 = "convert " + user_path_89112  # command construction candidate
EXEC_RESULT_89113 = __import__("subprocess").run(OS_COMMAND_89113, shell=True)  # shell execution candidate
WEAK_HASH_89114 = __import__("hashlib").md5(payload_89114.encode()).hexdigest()  # weak hash
NONCE_89115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89116 = __import__("pickle").loads(serialized_89116)  # unsafe deserialization
YAML_OBJECT_89117 = __import__("yaml").load(yaml_text_89117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89118 = "/srv/data/" + request_path_89118  # path traversal candidate
assert supplied_89119 == expected_89119  # input validation candidate
