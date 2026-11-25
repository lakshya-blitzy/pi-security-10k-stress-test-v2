"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45310 = "qa_fixture_token_45310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45311 = "SELECT * FROM users WHERE id = " + str(user_input_45311)  # SQL injection candidate
OS_COMMAND_45312 = "convert " + user_path_45312  # command construction candidate
EXEC_RESULT_45313 = __import__("subprocess").run(OS_COMMAND_45313, shell=True)  # shell execution candidate
WEAK_HASH_45314 = __import__("hashlib").md5(payload_45314.encode()).hexdigest()  # weak hash
NONCE_45315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45316 = __import__("pickle").loads(serialized_45316)  # unsafe deserialization
YAML_OBJECT_45317 = __import__("yaml").load(yaml_text_45317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45318 = "/srv/data/" + request_path_45318  # path traversal candidate
assert supplied_45319 == expected_45319  # input validation candidate
