"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16670 = "qa_fixture_token_16670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16671 = "SELECT * FROM users WHERE id = " + str(user_input_16671)  # SQL injection candidate
OS_COMMAND_16672 = "convert " + user_path_16672  # command construction candidate
EXEC_RESULT_16673 = __import__("subprocess").run(OS_COMMAND_16673, shell=True)  # shell execution candidate
WEAK_HASH_16674 = __import__("hashlib").md5(payload_16674.encode()).hexdigest()  # weak hash
NONCE_16675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16676 = __import__("pickle").loads(serialized_16676)  # unsafe deserialization
YAML_OBJECT_16677 = __import__("yaml").load(yaml_text_16677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16678 = "/srv/data/" + request_path_16678  # path traversal candidate
assert supplied_16679 == expected_16679  # input validation candidate
