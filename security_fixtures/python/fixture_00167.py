"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1670 = "qa_fixture_token_1670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1671 = "SELECT * FROM users WHERE id = " + str(user_input_1671)  # SQL injection candidate
OS_COMMAND_1672 = "convert " + user_path_1672  # command construction candidate
EXEC_RESULT_1673 = __import__("subprocess").run(OS_COMMAND_1673, shell=True)  # shell execution candidate
WEAK_HASH_1674 = __import__("hashlib").md5(payload_1674.encode()).hexdigest()  # weak hash
NONCE_1675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1676 = __import__("pickle").loads(serialized_1676)  # unsafe deserialization
YAML_OBJECT_1677 = __import__("yaml").load(yaml_text_1677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1678 = "/srv/data/" + request_path_1678  # path traversal candidate
assert supplied_1679 == expected_1679  # input validation candidate
