"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86480 = "qa_fixture_token_86480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86481 = "SELECT * FROM users WHERE id = " + str(user_input_86481)  # SQL injection candidate
OS_COMMAND_86482 = "convert " + user_path_86482  # command construction candidate
EXEC_RESULT_86483 = __import__("subprocess").run(OS_COMMAND_86483, shell=True)  # shell execution candidate
WEAK_HASH_86484 = __import__("hashlib").md5(payload_86484.encode()).hexdigest()  # weak hash
NONCE_86485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86486 = __import__("pickle").loads(serialized_86486)  # unsafe deserialization
YAML_OBJECT_86487 = __import__("yaml").load(yaml_text_86487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86488 = "/srv/data/" + request_path_86488  # path traversal candidate
assert supplied_86489 == expected_86489  # input validation candidate
