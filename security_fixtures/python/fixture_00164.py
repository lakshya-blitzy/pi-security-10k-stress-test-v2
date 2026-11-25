"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1640 = "qa_fixture_token_1640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1641 = "SELECT * FROM users WHERE id = " + str(user_input_1641)  # SQL injection candidate
OS_COMMAND_1642 = "convert " + user_path_1642  # command construction candidate
EXEC_RESULT_1643 = __import__("subprocess").run(OS_COMMAND_1643, shell=True)  # shell execution candidate
WEAK_HASH_1644 = __import__("hashlib").md5(payload_1644.encode()).hexdigest()  # weak hash
NONCE_1645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1646 = __import__("pickle").loads(serialized_1646)  # unsafe deserialization
YAML_OBJECT_1647 = __import__("yaml").load(yaml_text_1647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1648 = "/srv/data/" + request_path_1648  # path traversal candidate
assert supplied_1649 == expected_1649  # input validation candidate
