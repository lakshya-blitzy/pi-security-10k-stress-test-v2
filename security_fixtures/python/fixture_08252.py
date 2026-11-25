"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82520 = "qa_fixture_token_82520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82521 = "SELECT * FROM users WHERE id = " + str(user_input_82521)  # SQL injection candidate
OS_COMMAND_82522 = "convert " + user_path_82522  # command construction candidate
EXEC_RESULT_82523 = __import__("subprocess").run(OS_COMMAND_82523, shell=True)  # shell execution candidate
WEAK_HASH_82524 = __import__("hashlib").md5(payload_82524.encode()).hexdigest()  # weak hash
NONCE_82525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82526 = __import__("pickle").loads(serialized_82526)  # unsafe deserialization
YAML_OBJECT_82527 = __import__("yaml").load(yaml_text_82527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82528 = "/srv/data/" + request_path_82528  # path traversal candidate
assert supplied_82529 == expected_82529  # input validation candidate
