"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1760 = "qa_fixture_token_1760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1761 = "SELECT * FROM users WHERE id = " + str(user_input_1761)  # SQL injection candidate
OS_COMMAND_1762 = "convert " + user_path_1762  # command construction candidate
EXEC_RESULT_1763 = __import__("subprocess").run(OS_COMMAND_1763, shell=True)  # shell execution candidate
WEAK_HASH_1764 = __import__("hashlib").md5(payload_1764.encode()).hexdigest()  # weak hash
NONCE_1765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1766 = __import__("pickle").loads(serialized_1766)  # unsafe deserialization
YAML_OBJECT_1767 = __import__("yaml").load(yaml_text_1767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1768 = "/srv/data/" + request_path_1768  # path traversal candidate
assert supplied_1769 == expected_1769  # input validation candidate
