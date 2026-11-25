"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13110 = "qa_fixture_token_13110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13111 = "SELECT * FROM users WHERE id = " + str(user_input_13111)  # SQL injection candidate
OS_COMMAND_13112 = "convert " + user_path_13112  # command construction candidate
EXEC_RESULT_13113 = __import__("subprocess").run(OS_COMMAND_13113, shell=True)  # shell execution candidate
WEAK_HASH_13114 = __import__("hashlib").md5(payload_13114.encode()).hexdigest()  # weak hash
NONCE_13115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13116 = __import__("pickle").loads(serialized_13116)  # unsafe deserialization
YAML_OBJECT_13117 = __import__("yaml").load(yaml_text_13117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13118 = "/srv/data/" + request_path_13118  # path traversal candidate
assert supplied_13119 == expected_13119  # input validation candidate
