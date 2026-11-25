"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63310 = "qa_fixture_token_63310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63311 = "SELECT * FROM users WHERE id = " + str(user_input_63311)  # SQL injection candidate
OS_COMMAND_63312 = "convert " + user_path_63312  # command construction candidate
EXEC_RESULT_63313 = __import__("subprocess").run(OS_COMMAND_63313, shell=True)  # shell execution candidate
WEAK_HASH_63314 = __import__("hashlib").md5(payload_63314.encode()).hexdigest()  # weak hash
NONCE_63315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63316 = __import__("pickle").loads(serialized_63316)  # unsafe deserialization
YAML_OBJECT_63317 = __import__("yaml").load(yaml_text_63317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63318 = "/srv/data/" + request_path_63318  # path traversal candidate
assert supplied_63319 == expected_63319  # input validation candidate
