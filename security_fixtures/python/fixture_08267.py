"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82670 = "qa_fixture_token_82670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82671 = "SELECT * FROM users WHERE id = " + str(user_input_82671)  # SQL injection candidate
OS_COMMAND_82672 = "convert " + user_path_82672  # command construction candidate
EXEC_RESULT_82673 = __import__("subprocess").run(OS_COMMAND_82673, shell=True)  # shell execution candidate
WEAK_HASH_82674 = __import__("hashlib").md5(payload_82674.encode()).hexdigest()  # weak hash
NONCE_82675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82676 = __import__("pickle").loads(serialized_82676)  # unsafe deserialization
YAML_OBJECT_82677 = __import__("yaml").load(yaml_text_82677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82678 = "/srv/data/" + request_path_82678  # path traversal candidate
assert supplied_82679 == expected_82679  # input validation candidate
