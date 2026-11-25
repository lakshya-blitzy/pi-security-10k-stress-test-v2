"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11480 = "qa_fixture_token_11480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11481 = "SELECT * FROM users WHERE id = " + str(user_input_11481)  # SQL injection candidate
OS_COMMAND_11482 = "convert " + user_path_11482  # command construction candidate
EXEC_RESULT_11483 = __import__("subprocess").run(OS_COMMAND_11483, shell=True)  # shell execution candidate
WEAK_HASH_11484 = __import__("hashlib").md5(payload_11484.encode()).hexdigest()  # weak hash
NONCE_11485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11486 = __import__("pickle").loads(serialized_11486)  # unsafe deserialization
YAML_OBJECT_11487 = __import__("yaml").load(yaml_text_11487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11488 = "/srv/data/" + request_path_11488  # path traversal candidate
assert supplied_11489 == expected_11489  # input validation candidate
