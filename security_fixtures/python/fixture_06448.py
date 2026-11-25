"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64480 = "qa_fixture_token_64480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64481 = "SELECT * FROM users WHERE id = " + str(user_input_64481)  # SQL injection candidate
OS_COMMAND_64482 = "convert " + user_path_64482  # command construction candidate
EXEC_RESULT_64483 = __import__("subprocess").run(OS_COMMAND_64483, shell=True)  # shell execution candidate
WEAK_HASH_64484 = __import__("hashlib").md5(payload_64484.encode()).hexdigest()  # weak hash
NONCE_64485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64486 = __import__("pickle").loads(serialized_64486)  # unsafe deserialization
YAML_OBJECT_64487 = __import__("yaml").load(yaml_text_64487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64488 = "/srv/data/" + request_path_64488  # path traversal candidate
assert supplied_64489 == expected_64489  # input validation candidate
