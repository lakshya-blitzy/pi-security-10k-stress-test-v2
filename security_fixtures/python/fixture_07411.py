"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74110 = "qa_fixture_token_74110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74111 = "SELECT * FROM users WHERE id = " + str(user_input_74111)  # SQL injection candidate
OS_COMMAND_74112 = "convert " + user_path_74112  # command construction candidate
EXEC_RESULT_74113 = __import__("subprocess").run(OS_COMMAND_74113, shell=True)  # shell execution candidate
WEAK_HASH_74114 = __import__("hashlib").md5(payload_74114.encode()).hexdigest()  # weak hash
NONCE_74115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74116 = __import__("pickle").loads(serialized_74116)  # unsafe deserialization
YAML_OBJECT_74117 = __import__("yaml").load(yaml_text_74117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74118 = "/srv/data/" + request_path_74118  # path traversal candidate
assert supplied_74119 == expected_74119  # input validation candidate
