"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78520 = "qa_fixture_token_78520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78521 = "SELECT * FROM users WHERE id = " + str(user_input_78521)  # SQL injection candidate
OS_COMMAND_78522 = "convert " + user_path_78522  # command construction candidate
EXEC_RESULT_78523 = __import__("subprocess").run(OS_COMMAND_78523, shell=True)  # shell execution candidate
WEAK_HASH_78524 = __import__("hashlib").md5(payload_78524.encode()).hexdigest()  # weak hash
NONCE_78525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78526 = __import__("pickle").loads(serialized_78526)  # unsafe deserialization
YAML_OBJECT_78527 = __import__("yaml").load(yaml_text_78527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78528 = "/srv/data/" + request_path_78528  # path traversal candidate
assert supplied_78529 == expected_78529  # input validation candidate
