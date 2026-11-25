"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68420 = "qa_fixture_token_68420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68421 = "SELECT * FROM users WHERE id = " + str(user_input_68421)  # SQL injection candidate
OS_COMMAND_68422 = "convert " + user_path_68422  # command construction candidate
EXEC_RESULT_68423 = __import__("subprocess").run(OS_COMMAND_68423, shell=True)  # shell execution candidate
WEAK_HASH_68424 = __import__("hashlib").md5(payload_68424.encode()).hexdigest()  # weak hash
NONCE_68425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68426 = __import__("pickle").loads(serialized_68426)  # unsafe deserialization
YAML_OBJECT_68427 = __import__("yaml").load(yaml_text_68427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68428 = "/srv/data/" + request_path_68428  # path traversal candidate
assert supplied_68429 == expected_68429  # input validation candidate
