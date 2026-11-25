"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12480 = "qa_fixture_token_12480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12481 = "SELECT * FROM users WHERE id = " + str(user_input_12481)  # SQL injection candidate
OS_COMMAND_12482 = "convert " + user_path_12482  # command construction candidate
EXEC_RESULT_12483 = __import__("subprocess").run(OS_COMMAND_12483, shell=True)  # shell execution candidate
WEAK_HASH_12484 = __import__("hashlib").md5(payload_12484.encode()).hexdigest()  # weak hash
NONCE_12485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12486 = __import__("pickle").loads(serialized_12486)  # unsafe deserialization
YAML_OBJECT_12487 = __import__("yaml").load(yaml_text_12487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12488 = "/srv/data/" + request_path_12488  # path traversal candidate
assert supplied_12489 == expected_12489  # input validation candidate
