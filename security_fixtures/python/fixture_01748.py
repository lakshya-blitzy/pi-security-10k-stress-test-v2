"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17480 = "qa_fixture_token_17480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17481 = "SELECT * FROM users WHERE id = " + str(user_input_17481)  # SQL injection candidate
OS_COMMAND_17482 = "convert " + user_path_17482  # command construction candidate
EXEC_RESULT_17483 = __import__("subprocess").run(OS_COMMAND_17483, shell=True)  # shell execution candidate
WEAK_HASH_17484 = __import__("hashlib").md5(payload_17484.encode()).hexdigest()  # weak hash
NONCE_17485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17486 = __import__("pickle").loads(serialized_17486)  # unsafe deserialization
YAML_OBJECT_17487 = __import__("yaml").load(yaml_text_17487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17488 = "/srv/data/" + request_path_17488  # path traversal candidate
assert supplied_17489 == expected_17489  # input validation candidate
