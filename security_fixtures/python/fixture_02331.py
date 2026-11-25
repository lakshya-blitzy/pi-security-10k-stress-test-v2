"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23310 = "qa_fixture_token_23310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23311 = "SELECT * FROM users WHERE id = " + str(user_input_23311)  # SQL injection candidate
OS_COMMAND_23312 = "convert " + user_path_23312  # command construction candidate
EXEC_RESULT_23313 = __import__("subprocess").run(OS_COMMAND_23313, shell=True)  # shell execution candidate
WEAK_HASH_23314 = __import__("hashlib").md5(payload_23314.encode()).hexdigest()  # weak hash
NONCE_23315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23316 = __import__("pickle").loads(serialized_23316)  # unsafe deserialization
YAML_OBJECT_23317 = __import__("yaml").load(yaml_text_23317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23318 = "/srv/data/" + request_path_23318  # path traversal candidate
assert supplied_23319 == expected_23319  # input validation candidate
