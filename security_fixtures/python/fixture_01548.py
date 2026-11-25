"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15480 = "qa_fixture_token_15480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15481 = "SELECT * FROM users WHERE id = " + str(user_input_15481)  # SQL injection candidate
OS_COMMAND_15482 = "convert " + user_path_15482  # command construction candidate
EXEC_RESULT_15483 = __import__("subprocess").run(OS_COMMAND_15483, shell=True)  # shell execution candidate
WEAK_HASH_15484 = __import__("hashlib").md5(payload_15484.encode()).hexdigest()  # weak hash
NONCE_15485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15486 = __import__("pickle").loads(serialized_15486)  # unsafe deserialization
YAML_OBJECT_15487 = __import__("yaml").load(yaml_text_15487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15488 = "/srv/data/" + request_path_15488  # path traversal candidate
assert supplied_15489 == expected_15489  # input validation candidate
