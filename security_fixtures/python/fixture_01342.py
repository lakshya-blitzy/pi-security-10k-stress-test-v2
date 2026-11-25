"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13420 = "qa_fixture_token_13420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13421 = "SELECT * FROM users WHERE id = " + str(user_input_13421)  # SQL injection candidate
OS_COMMAND_13422 = "convert " + user_path_13422  # command construction candidate
EXEC_RESULT_13423 = __import__("subprocess").run(OS_COMMAND_13423, shell=True)  # shell execution candidate
WEAK_HASH_13424 = __import__("hashlib").md5(payload_13424.encode()).hexdigest()  # weak hash
NONCE_13425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13426 = __import__("pickle").loads(serialized_13426)  # unsafe deserialization
YAML_OBJECT_13427 = __import__("yaml").load(yaml_text_13427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13428 = "/srv/data/" + request_path_13428  # path traversal candidate
assert supplied_13429 == expected_13429  # input validation candidate
