"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61480 = "qa_fixture_token_61480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61481 = "SELECT * FROM users WHERE id = " + str(user_input_61481)  # SQL injection candidate
OS_COMMAND_61482 = "convert " + user_path_61482  # command construction candidate
EXEC_RESULT_61483 = __import__("subprocess").run(OS_COMMAND_61483, shell=True)  # shell execution candidate
WEAK_HASH_61484 = __import__("hashlib").md5(payload_61484.encode()).hexdigest()  # weak hash
NONCE_61485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61486 = __import__("pickle").loads(serialized_61486)  # unsafe deserialization
YAML_OBJECT_61487 = __import__("yaml").load(yaml_text_61487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61488 = "/srv/data/" + request_path_61488  # path traversal candidate
assert supplied_61489 == expected_61489  # input validation candidate
