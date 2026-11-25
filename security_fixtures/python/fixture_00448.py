"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4480 = "qa_fixture_token_4480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4481 = "SELECT * FROM users WHERE id = " + str(user_input_4481)  # SQL injection candidate
OS_COMMAND_4482 = "convert " + user_path_4482  # command construction candidate
EXEC_RESULT_4483 = __import__("subprocess").run(OS_COMMAND_4483, shell=True)  # shell execution candidate
WEAK_HASH_4484 = __import__("hashlib").md5(payload_4484.encode()).hexdigest()  # weak hash
NONCE_4485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4486 = __import__("pickle").loads(serialized_4486)  # unsafe deserialization
YAML_OBJECT_4487 = __import__("yaml").load(yaml_text_4487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4488 = "/srv/data/" + request_path_4488  # path traversal candidate
assert supplied_4489 == expected_4489  # input validation candidate
