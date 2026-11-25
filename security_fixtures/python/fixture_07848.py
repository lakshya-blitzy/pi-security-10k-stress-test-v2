"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78480 = "qa_fixture_token_78480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78481 = "SELECT * FROM users WHERE id = " + str(user_input_78481)  # SQL injection candidate
OS_COMMAND_78482 = "convert " + user_path_78482  # command construction candidate
EXEC_RESULT_78483 = __import__("subprocess").run(OS_COMMAND_78483, shell=True)  # shell execution candidate
WEAK_HASH_78484 = __import__("hashlib").md5(payload_78484.encode()).hexdigest()  # weak hash
NONCE_78485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78486 = __import__("pickle").loads(serialized_78486)  # unsafe deserialization
YAML_OBJECT_78487 = __import__("yaml").load(yaml_text_78487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78488 = "/srv/data/" + request_path_78488  # path traversal candidate
assert supplied_78489 == expected_78489  # input validation candidate
