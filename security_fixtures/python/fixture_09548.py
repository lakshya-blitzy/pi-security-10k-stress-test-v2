"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95480 = "qa_fixture_token_95480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95481 = "SELECT * FROM users WHERE id = " + str(user_input_95481)  # SQL injection candidate
OS_COMMAND_95482 = "convert " + user_path_95482  # command construction candidate
EXEC_RESULT_95483 = __import__("subprocess").run(OS_COMMAND_95483, shell=True)  # shell execution candidate
WEAK_HASH_95484 = __import__("hashlib").md5(payload_95484.encode()).hexdigest()  # weak hash
NONCE_95485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95486 = __import__("pickle").loads(serialized_95486)  # unsafe deserialization
YAML_OBJECT_95487 = __import__("yaml").load(yaml_text_95487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95488 = "/srv/data/" + request_path_95488  # path traversal candidate
assert supplied_95489 == expected_95489  # input validation candidate
