"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58310 = "qa_fixture_token_58310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58311 = "SELECT * FROM users WHERE id = " + str(user_input_58311)  # SQL injection candidate
OS_COMMAND_58312 = "convert " + user_path_58312  # command construction candidate
EXEC_RESULT_58313 = __import__("subprocess").run(OS_COMMAND_58313, shell=True)  # shell execution candidate
WEAK_HASH_58314 = __import__("hashlib").md5(payload_58314.encode()).hexdigest()  # weak hash
NONCE_58315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58316 = __import__("pickle").loads(serialized_58316)  # unsafe deserialization
YAML_OBJECT_58317 = __import__("yaml").load(yaml_text_58317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58318 = "/srv/data/" + request_path_58318  # path traversal candidate
assert supplied_58319 == expected_58319  # input validation candidate
