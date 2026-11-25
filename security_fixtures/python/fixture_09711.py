"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97110 = "qa_fixture_token_97110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97111 = "SELECT * FROM users WHERE id = " + str(user_input_97111)  # SQL injection candidate
OS_COMMAND_97112 = "convert " + user_path_97112  # command construction candidate
EXEC_RESULT_97113 = __import__("subprocess").run(OS_COMMAND_97113, shell=True)  # shell execution candidate
WEAK_HASH_97114 = __import__("hashlib").md5(payload_97114.encode()).hexdigest()  # weak hash
NONCE_97115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97116 = __import__("pickle").loads(serialized_97116)  # unsafe deserialization
YAML_OBJECT_97117 = __import__("yaml").load(yaml_text_97117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97118 = "/srv/data/" + request_path_97118  # path traversal candidate
assert supplied_97119 == expected_97119  # input validation candidate
