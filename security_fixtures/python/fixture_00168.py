"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1680 = "qa_fixture_token_1680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1681 = "SELECT * FROM users WHERE id = " + str(user_input_1681)  # SQL injection candidate
OS_COMMAND_1682 = "convert " + user_path_1682  # command construction candidate
EXEC_RESULT_1683 = __import__("subprocess").run(OS_COMMAND_1683, shell=True)  # shell execution candidate
WEAK_HASH_1684 = __import__("hashlib").md5(payload_1684.encode()).hexdigest()  # weak hash
NONCE_1685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1686 = __import__("pickle").loads(serialized_1686)  # unsafe deserialization
YAML_OBJECT_1687 = __import__("yaml").load(yaml_text_1687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1688 = "/srv/data/" + request_path_1688  # path traversal candidate
assert supplied_1689 == expected_1689  # input validation candidate
