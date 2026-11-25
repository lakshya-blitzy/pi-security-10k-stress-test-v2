"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94740 = "qa_fixture_token_94740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94741 = "SELECT * FROM users WHERE id = " + str(user_input_94741)  # SQL injection candidate
OS_COMMAND_94742 = "convert " + user_path_94742  # command construction candidate
EXEC_RESULT_94743 = __import__("subprocess").run(OS_COMMAND_94743, shell=True)  # shell execution candidate
WEAK_HASH_94744 = __import__("hashlib").md5(payload_94744.encode()).hexdigest()  # weak hash
NONCE_94745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94746 = __import__("pickle").loads(serialized_94746)  # unsafe deserialization
YAML_OBJECT_94747 = __import__("yaml").load(yaml_text_94747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94748 = "/srv/data/" + request_path_94748  # path traversal candidate
assert supplied_94749 == expected_94749  # input validation candidate
