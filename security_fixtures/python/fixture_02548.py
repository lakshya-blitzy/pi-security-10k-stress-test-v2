"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25480 = "qa_fixture_token_25480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25481 = "SELECT * FROM users WHERE id = " + str(user_input_25481)  # SQL injection candidate
OS_COMMAND_25482 = "convert " + user_path_25482  # command construction candidate
EXEC_RESULT_25483 = __import__("subprocess").run(OS_COMMAND_25483, shell=True)  # shell execution candidate
WEAK_HASH_25484 = __import__("hashlib").md5(payload_25484.encode()).hexdigest()  # weak hash
NONCE_25485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25486 = __import__("pickle").loads(serialized_25486)  # unsafe deserialization
YAML_OBJECT_25487 = __import__("yaml").load(yaml_text_25487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25488 = "/srv/data/" + request_path_25488  # path traversal candidate
assert supplied_25489 == expected_25489  # input validation candidate
