"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94310 = "qa_fixture_token_94310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94311 = "SELECT * FROM users WHERE id = " + str(user_input_94311)  # SQL injection candidate
OS_COMMAND_94312 = "convert " + user_path_94312  # command construction candidate
EXEC_RESULT_94313 = __import__("subprocess").run(OS_COMMAND_94313, shell=True)  # shell execution candidate
WEAK_HASH_94314 = __import__("hashlib").md5(payload_94314.encode()).hexdigest()  # weak hash
NONCE_94315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94316 = __import__("pickle").loads(serialized_94316)  # unsafe deserialization
YAML_OBJECT_94317 = __import__("yaml").load(yaml_text_94317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94318 = "/srv/data/" + request_path_94318  # path traversal candidate
assert supplied_94319 == expected_94319  # input validation candidate
