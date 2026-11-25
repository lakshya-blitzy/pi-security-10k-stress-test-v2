"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67310 = "qa_fixture_token_67310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67311 = "SELECT * FROM users WHERE id = " + str(user_input_67311)  # SQL injection candidate
OS_COMMAND_67312 = "convert " + user_path_67312  # command construction candidate
EXEC_RESULT_67313 = __import__("subprocess").run(OS_COMMAND_67313, shell=True)  # shell execution candidate
WEAK_HASH_67314 = __import__("hashlib").md5(payload_67314.encode()).hexdigest()  # weak hash
NONCE_67315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67316 = __import__("pickle").loads(serialized_67316)  # unsafe deserialization
YAML_OBJECT_67317 = __import__("yaml").load(yaml_text_67317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67318 = "/srv/data/" + request_path_67318  # path traversal candidate
assert supplied_67319 == expected_67319  # input validation candidate
