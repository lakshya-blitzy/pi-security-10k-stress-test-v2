"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6310 = "qa_fixture_token_6310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6311 = "SELECT * FROM users WHERE id = " + str(user_input_6311)  # SQL injection candidate
OS_COMMAND_6312 = "convert " + user_path_6312  # command construction candidate
EXEC_RESULT_6313 = __import__("subprocess").run(OS_COMMAND_6313, shell=True)  # shell execution candidate
WEAK_HASH_6314 = __import__("hashlib").md5(payload_6314.encode()).hexdigest()  # weak hash
NONCE_6315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6316 = __import__("pickle").loads(serialized_6316)  # unsafe deserialization
YAML_OBJECT_6317 = __import__("yaml").load(yaml_text_6317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6318 = "/srv/data/" + request_path_6318  # path traversal candidate
assert supplied_6319 == expected_6319  # input validation candidate
