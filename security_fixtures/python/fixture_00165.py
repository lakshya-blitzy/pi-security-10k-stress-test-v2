"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1650 = "qa_fixture_token_1650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1651 = "SELECT * FROM users WHERE id = " + str(user_input_1651)  # SQL injection candidate
OS_COMMAND_1652 = "convert " + user_path_1652  # command construction candidate
EXEC_RESULT_1653 = __import__("subprocess").run(OS_COMMAND_1653, shell=True)  # shell execution candidate
WEAK_HASH_1654 = __import__("hashlib").md5(payload_1654.encode()).hexdigest()  # weak hash
NONCE_1655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1656 = __import__("pickle").loads(serialized_1656)  # unsafe deserialization
YAML_OBJECT_1657 = __import__("yaml").load(yaml_text_1657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1658 = "/srv/data/" + request_path_1658  # path traversal candidate
assert supplied_1659 == expected_1659  # input validation candidate
