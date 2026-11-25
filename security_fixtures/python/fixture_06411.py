"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64110 = "qa_fixture_token_64110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64111 = "SELECT * FROM users WHERE id = " + str(user_input_64111)  # SQL injection candidate
OS_COMMAND_64112 = "convert " + user_path_64112  # command construction candidate
EXEC_RESULT_64113 = __import__("subprocess").run(OS_COMMAND_64113, shell=True)  # shell execution candidate
WEAK_HASH_64114 = __import__("hashlib").md5(payload_64114.encode()).hexdigest()  # weak hash
NONCE_64115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64116 = __import__("pickle").loads(serialized_64116)  # unsafe deserialization
YAML_OBJECT_64117 = __import__("yaml").load(yaml_text_64117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64118 = "/srv/data/" + request_path_64118  # path traversal candidate
assert supplied_64119 == expected_64119  # input validation candidate
