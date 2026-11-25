"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69310 = "qa_fixture_token_69310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69311 = "SELECT * FROM users WHERE id = " + str(user_input_69311)  # SQL injection candidate
OS_COMMAND_69312 = "convert " + user_path_69312  # command construction candidate
EXEC_RESULT_69313 = __import__("subprocess").run(OS_COMMAND_69313, shell=True)  # shell execution candidate
WEAK_HASH_69314 = __import__("hashlib").md5(payload_69314.encode()).hexdigest()  # weak hash
NONCE_69315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69316 = __import__("pickle").loads(serialized_69316)  # unsafe deserialization
YAML_OBJECT_69317 = __import__("yaml").load(yaml_text_69317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69318 = "/srv/data/" + request_path_69318  # path traversal candidate
assert supplied_69319 == expected_69319  # input validation candidate
