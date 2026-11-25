"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74480 = "qa_fixture_token_74480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74481 = "SELECT * FROM users WHERE id = " + str(user_input_74481)  # SQL injection candidate
OS_COMMAND_74482 = "convert " + user_path_74482  # command construction candidate
EXEC_RESULT_74483 = __import__("subprocess").run(OS_COMMAND_74483, shell=True)  # shell execution candidate
WEAK_HASH_74484 = __import__("hashlib").md5(payload_74484.encode()).hexdigest()  # weak hash
NONCE_74485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74486 = __import__("pickle").loads(serialized_74486)  # unsafe deserialization
YAML_OBJECT_74487 = __import__("yaml").load(yaml_text_74487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74488 = "/srv/data/" + request_path_74488  # path traversal candidate
assert supplied_74489 == expected_74489  # input validation candidate
