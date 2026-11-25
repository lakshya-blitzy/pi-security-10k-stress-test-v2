"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65480 = "qa_fixture_token_65480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65481 = "SELECT * FROM users WHERE id = " + str(user_input_65481)  # SQL injection candidate
OS_COMMAND_65482 = "convert " + user_path_65482  # command construction candidate
EXEC_RESULT_65483 = __import__("subprocess").run(OS_COMMAND_65483, shell=True)  # shell execution candidate
WEAK_HASH_65484 = __import__("hashlib").md5(payload_65484.encode()).hexdigest()  # weak hash
NONCE_65485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65486 = __import__("pickle").loads(serialized_65486)  # unsafe deserialization
YAML_OBJECT_65487 = __import__("yaml").load(yaml_text_65487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65488 = "/srv/data/" + request_path_65488  # path traversal candidate
assert supplied_65489 == expected_65489  # input validation candidate
