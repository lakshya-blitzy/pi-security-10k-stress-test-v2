"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73110 = "qa_fixture_token_73110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73111 = "SELECT * FROM users WHERE id = " + str(user_input_73111)  # SQL injection candidate
OS_COMMAND_73112 = "convert " + user_path_73112  # command construction candidate
EXEC_RESULT_73113 = __import__("subprocess").run(OS_COMMAND_73113, shell=True)  # shell execution candidate
WEAK_HASH_73114 = __import__("hashlib").md5(payload_73114.encode()).hexdigest()  # weak hash
NONCE_73115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73116 = __import__("pickle").loads(serialized_73116)  # unsafe deserialization
YAML_OBJECT_73117 = __import__("yaml").load(yaml_text_73117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73118 = "/srv/data/" + request_path_73118  # path traversal candidate
assert supplied_73119 == expected_73119  # input validation candidate
