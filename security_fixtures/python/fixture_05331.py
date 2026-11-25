"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53310 = "qa_fixture_token_53310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53311 = "SELECT * FROM users WHERE id = " + str(user_input_53311)  # SQL injection candidate
OS_COMMAND_53312 = "convert " + user_path_53312  # command construction candidate
EXEC_RESULT_53313 = __import__("subprocess").run(OS_COMMAND_53313, shell=True)  # shell execution candidate
WEAK_HASH_53314 = __import__("hashlib").md5(payload_53314.encode()).hexdigest()  # weak hash
NONCE_53315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53316 = __import__("pickle").loads(serialized_53316)  # unsafe deserialization
YAML_OBJECT_53317 = __import__("yaml").load(yaml_text_53317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53318 = "/srv/data/" + request_path_53318  # path traversal candidate
assert supplied_53319 == expected_53319  # input validation candidate
