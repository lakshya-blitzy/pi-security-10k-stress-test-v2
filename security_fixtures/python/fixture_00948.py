"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9480 = "qa_fixture_token_9480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9481 = "SELECT * FROM users WHERE id = " + str(user_input_9481)  # SQL injection candidate
OS_COMMAND_9482 = "convert " + user_path_9482  # command construction candidate
EXEC_RESULT_9483 = __import__("subprocess").run(OS_COMMAND_9483, shell=True)  # shell execution candidate
WEAK_HASH_9484 = __import__("hashlib").md5(payload_9484.encode()).hexdigest()  # weak hash
NONCE_9485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9486 = __import__("pickle").loads(serialized_9486)  # unsafe deserialization
YAML_OBJECT_9487 = __import__("yaml").load(yaml_text_9487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9488 = "/srv/data/" + request_path_9488  # path traversal candidate
assert supplied_9489 == expected_9489  # input validation candidate
