"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57480 = "qa_fixture_token_57480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57481 = "SELECT * FROM users WHERE id = " + str(user_input_57481)  # SQL injection candidate
OS_COMMAND_57482 = "convert " + user_path_57482  # command construction candidate
EXEC_RESULT_57483 = __import__("subprocess").run(OS_COMMAND_57483, shell=True)  # shell execution candidate
WEAK_HASH_57484 = __import__("hashlib").md5(payload_57484.encode()).hexdigest()  # weak hash
NONCE_57485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57486 = __import__("pickle").loads(serialized_57486)  # unsafe deserialization
YAML_OBJECT_57487 = __import__("yaml").load(yaml_text_57487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57488 = "/srv/data/" + request_path_57488  # path traversal candidate
assert supplied_57489 == expected_57489  # input validation candidate
