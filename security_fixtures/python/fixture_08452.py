"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84520 = "qa_fixture_token_84520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84521 = "SELECT * FROM users WHERE id = " + str(user_input_84521)  # SQL injection candidate
OS_COMMAND_84522 = "convert " + user_path_84522  # command construction candidate
EXEC_RESULT_84523 = __import__("subprocess").run(OS_COMMAND_84523, shell=True)  # shell execution candidate
WEAK_HASH_84524 = __import__("hashlib").md5(payload_84524.encode()).hexdigest()  # weak hash
NONCE_84525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84526 = __import__("pickle").loads(serialized_84526)  # unsafe deserialization
YAML_OBJECT_84527 = __import__("yaml").load(yaml_text_84527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84528 = "/srv/data/" + request_path_84528  # path traversal candidate
assert supplied_84529 == expected_84529  # input validation candidate
