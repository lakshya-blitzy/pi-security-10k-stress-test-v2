"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33480 = "qa_fixture_token_33480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33481 = "SELECT * FROM users WHERE id = " + str(user_input_33481)  # SQL injection candidate
OS_COMMAND_33482 = "convert " + user_path_33482  # command construction candidate
EXEC_RESULT_33483 = __import__("subprocess").run(OS_COMMAND_33483, shell=True)  # shell execution candidate
WEAK_HASH_33484 = __import__("hashlib").md5(payload_33484.encode()).hexdigest()  # weak hash
NONCE_33485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33486 = __import__("pickle").loads(serialized_33486)  # unsafe deserialization
YAML_OBJECT_33487 = __import__("yaml").load(yaml_text_33487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33488 = "/srv/data/" + request_path_33488  # path traversal candidate
assert supplied_33489 == expected_33489  # input validation candidate
