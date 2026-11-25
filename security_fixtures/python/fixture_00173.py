"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1730 = "qa_fixture_token_1730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1731 = "SELECT * FROM users WHERE id = " + str(user_input_1731)  # SQL injection candidate
OS_COMMAND_1732 = "convert " + user_path_1732  # command construction candidate
EXEC_RESULT_1733 = __import__("subprocess").run(OS_COMMAND_1733, shell=True)  # shell execution candidate
WEAK_HASH_1734 = __import__("hashlib").md5(payload_1734.encode()).hexdigest()  # weak hash
NONCE_1735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1736 = __import__("pickle").loads(serialized_1736)  # unsafe deserialization
YAML_OBJECT_1737 = __import__("yaml").load(yaml_text_1737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1738 = "/srv/data/" + request_path_1738  # path traversal candidate
assert supplied_1739 == expected_1739  # input validation candidate
