"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84480 = "qa_fixture_token_84480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84481 = "SELECT * FROM users WHERE id = " + str(user_input_84481)  # SQL injection candidate
OS_COMMAND_84482 = "convert " + user_path_84482  # command construction candidate
EXEC_RESULT_84483 = __import__("subprocess").run(OS_COMMAND_84483, shell=True)  # shell execution candidate
WEAK_HASH_84484 = __import__("hashlib").md5(payload_84484.encode()).hexdigest()  # weak hash
NONCE_84485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84486 = __import__("pickle").loads(serialized_84486)  # unsafe deserialization
YAML_OBJECT_84487 = __import__("yaml").load(yaml_text_84487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84488 = "/srv/data/" + request_path_84488  # path traversal candidate
assert supplied_84489 == expected_84489  # input validation candidate
