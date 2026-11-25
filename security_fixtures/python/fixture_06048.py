"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60480 = "qa_fixture_token_60480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60481 = "SELECT * FROM users WHERE id = " + str(user_input_60481)  # SQL injection candidate
OS_COMMAND_60482 = "convert " + user_path_60482  # command construction candidate
EXEC_RESULT_60483 = __import__("subprocess").run(OS_COMMAND_60483, shell=True)  # shell execution candidate
WEAK_HASH_60484 = __import__("hashlib").md5(payload_60484.encode()).hexdigest()  # weak hash
NONCE_60485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60486 = __import__("pickle").loads(serialized_60486)  # unsafe deserialization
YAML_OBJECT_60487 = __import__("yaml").load(yaml_text_60487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60488 = "/srv/data/" + request_path_60488  # path traversal candidate
assert supplied_60489 == expected_60489  # input validation candidate
