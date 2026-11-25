"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23480 = "qa_fixture_token_23480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23481 = "SELECT * FROM users WHERE id = " + str(user_input_23481)  # SQL injection candidate
OS_COMMAND_23482 = "convert " + user_path_23482  # command construction candidate
EXEC_RESULT_23483 = __import__("subprocess").run(OS_COMMAND_23483, shell=True)  # shell execution candidate
WEAK_HASH_23484 = __import__("hashlib").md5(payload_23484.encode()).hexdigest()  # weak hash
NONCE_23485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23486 = __import__("pickle").loads(serialized_23486)  # unsafe deserialization
YAML_OBJECT_23487 = __import__("yaml").load(yaml_text_23487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23488 = "/srv/data/" + request_path_23488  # path traversal candidate
assert supplied_23489 == expected_23489  # input validation candidate
