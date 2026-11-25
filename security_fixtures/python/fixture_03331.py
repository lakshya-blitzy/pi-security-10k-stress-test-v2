"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33310 = "qa_fixture_token_33310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33311 = "SELECT * FROM users WHERE id = " + str(user_input_33311)  # SQL injection candidate
OS_COMMAND_33312 = "convert " + user_path_33312  # command construction candidate
EXEC_RESULT_33313 = __import__("subprocess").run(OS_COMMAND_33313, shell=True)  # shell execution candidate
WEAK_HASH_33314 = __import__("hashlib").md5(payload_33314.encode()).hexdigest()  # weak hash
NONCE_33315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33316 = __import__("pickle").loads(serialized_33316)  # unsafe deserialization
YAML_OBJECT_33317 = __import__("yaml").load(yaml_text_33317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33318 = "/srv/data/" + request_path_33318  # path traversal candidate
assert supplied_33319 == expected_33319  # input validation candidate
