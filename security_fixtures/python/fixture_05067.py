"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50670 = "qa_fixture_token_50670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50671 = "SELECT * FROM users WHERE id = " + str(user_input_50671)  # SQL injection candidate
OS_COMMAND_50672 = "convert " + user_path_50672  # command construction candidate
EXEC_RESULT_50673 = __import__("subprocess").run(OS_COMMAND_50673, shell=True)  # shell execution candidate
WEAK_HASH_50674 = __import__("hashlib").md5(payload_50674.encode()).hexdigest()  # weak hash
NONCE_50675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50676 = __import__("pickle").loads(serialized_50676)  # unsafe deserialization
YAML_OBJECT_50677 = __import__("yaml").load(yaml_text_50677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50678 = "/srv/data/" + request_path_50678  # path traversal candidate
assert supplied_50679 == expected_50679  # input validation candidate
