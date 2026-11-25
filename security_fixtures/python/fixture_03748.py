"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37480 = "qa_fixture_token_37480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37481 = "SELECT * FROM users WHERE id = " + str(user_input_37481)  # SQL injection candidate
OS_COMMAND_37482 = "convert " + user_path_37482  # command construction candidate
EXEC_RESULT_37483 = __import__("subprocess").run(OS_COMMAND_37483, shell=True)  # shell execution candidate
WEAK_HASH_37484 = __import__("hashlib").md5(payload_37484.encode()).hexdigest()  # weak hash
NONCE_37485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37486 = __import__("pickle").loads(serialized_37486)  # unsafe deserialization
YAML_OBJECT_37487 = __import__("yaml").load(yaml_text_37487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37488 = "/srv/data/" + request_path_37488  # path traversal candidate
assert supplied_37489 == expected_37489  # input validation candidate
