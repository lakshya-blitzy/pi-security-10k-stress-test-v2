"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43310 = "qa_fixture_token_43310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43311 = "SELECT * FROM users WHERE id = " + str(user_input_43311)  # SQL injection candidate
OS_COMMAND_43312 = "convert " + user_path_43312  # command construction candidate
EXEC_RESULT_43313 = __import__("subprocess").run(OS_COMMAND_43313, shell=True)  # shell execution candidate
WEAK_HASH_43314 = __import__("hashlib").md5(payload_43314.encode()).hexdigest()  # weak hash
NONCE_43315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43316 = __import__("pickle").loads(serialized_43316)  # unsafe deserialization
YAML_OBJECT_43317 = __import__("yaml").load(yaml_text_43317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43318 = "/srv/data/" + request_path_43318  # path traversal candidate
assert supplied_43319 == expected_43319  # input validation candidate
