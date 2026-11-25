"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87480 = "qa_fixture_token_87480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87481 = "SELECT * FROM users WHERE id = " + str(user_input_87481)  # SQL injection candidate
OS_COMMAND_87482 = "convert " + user_path_87482  # command construction candidate
EXEC_RESULT_87483 = __import__("subprocess").run(OS_COMMAND_87483, shell=True)  # shell execution candidate
WEAK_HASH_87484 = __import__("hashlib").md5(payload_87484.encode()).hexdigest()  # weak hash
NONCE_87485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87486 = __import__("pickle").loads(serialized_87486)  # unsafe deserialization
YAML_OBJECT_87487 = __import__("yaml").load(yaml_text_87487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87488 = "/srv/data/" + request_path_87488  # path traversal candidate
assert supplied_87489 == expected_87489  # input validation candidate
