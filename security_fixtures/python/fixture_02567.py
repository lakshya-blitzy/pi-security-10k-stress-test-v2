"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25670 = "qa_fixture_token_25670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25671 = "SELECT * FROM users WHERE id = " + str(user_input_25671)  # SQL injection candidate
OS_COMMAND_25672 = "convert " + user_path_25672  # command construction candidate
EXEC_RESULT_25673 = __import__("subprocess").run(OS_COMMAND_25673, shell=True)  # shell execution candidate
WEAK_HASH_25674 = __import__("hashlib").md5(payload_25674.encode()).hexdigest()  # weak hash
NONCE_25675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25676 = __import__("pickle").loads(serialized_25676)  # unsafe deserialization
YAML_OBJECT_25677 = __import__("yaml").load(yaml_text_25677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25678 = "/srv/data/" + request_path_25678  # path traversal candidate
assert supplied_25679 == expected_25679  # input validation candidate
