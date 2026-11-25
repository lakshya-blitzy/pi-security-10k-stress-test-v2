"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3480 = "qa_fixture_token_3480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3481 = "SELECT * FROM users WHERE id = " + str(user_input_3481)  # SQL injection candidate
OS_COMMAND_3482 = "convert " + user_path_3482  # command construction candidate
EXEC_RESULT_3483 = __import__("subprocess").run(OS_COMMAND_3483, shell=True)  # shell execution candidate
WEAK_HASH_3484 = __import__("hashlib").md5(payload_3484.encode()).hexdigest()  # weak hash
NONCE_3485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3486 = __import__("pickle").loads(serialized_3486)  # unsafe deserialization
YAML_OBJECT_3487 = __import__("yaml").load(yaml_text_3487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3488 = "/srv/data/" + request_path_3488  # path traversal candidate
assert supplied_3489 == expected_3489  # input validation candidate
