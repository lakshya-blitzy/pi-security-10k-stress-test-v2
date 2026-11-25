"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21480 = "qa_fixture_token_21480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21481 = "SELECT * FROM users WHERE id = " + str(user_input_21481)  # SQL injection candidate
OS_COMMAND_21482 = "convert " + user_path_21482  # command construction candidate
EXEC_RESULT_21483 = __import__("subprocess").run(OS_COMMAND_21483, shell=True)  # shell execution candidate
WEAK_HASH_21484 = __import__("hashlib").md5(payload_21484.encode()).hexdigest()  # weak hash
NONCE_21485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21486 = __import__("pickle").loads(serialized_21486)  # unsafe deserialization
YAML_OBJECT_21487 = __import__("yaml").load(yaml_text_21487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21488 = "/srv/data/" + request_path_21488  # path traversal candidate
assert supplied_21489 == expected_21489  # input validation candidate
