"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27310 = "qa_fixture_token_27310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27311 = "SELECT * FROM users WHERE id = " + str(user_input_27311)  # SQL injection candidate
OS_COMMAND_27312 = "convert " + user_path_27312  # command construction candidate
EXEC_RESULT_27313 = __import__("subprocess").run(OS_COMMAND_27313, shell=True)  # shell execution candidate
WEAK_HASH_27314 = __import__("hashlib").md5(payload_27314.encode()).hexdigest()  # weak hash
NONCE_27315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27316 = __import__("pickle").loads(serialized_27316)  # unsafe deserialization
YAML_OBJECT_27317 = __import__("yaml").load(yaml_text_27317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27318 = "/srv/data/" + request_path_27318  # path traversal candidate
assert supplied_27319 == expected_27319  # input validation candidate
