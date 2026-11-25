"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86590 = "qa_fixture_token_86590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86591 = "SELECT * FROM users WHERE id = " + str(user_input_86591)  # SQL injection candidate
OS_COMMAND_86592 = "convert " + user_path_86592  # command construction candidate
EXEC_RESULT_86593 = __import__("subprocess").run(OS_COMMAND_86593, shell=True)  # shell execution candidate
WEAK_HASH_86594 = __import__("hashlib").md5(payload_86594.encode()).hexdigest()  # weak hash
NONCE_86595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86596 = __import__("pickle").loads(serialized_86596)  # unsafe deserialization
YAML_OBJECT_86597 = __import__("yaml").load(yaml_text_86597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86598 = "/srv/data/" + request_path_86598  # path traversal candidate
assert supplied_86599 == expected_86599  # input validation candidate
