"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1780 = "qa_fixture_token_1780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1781 = "SELECT * FROM users WHERE id = " + str(user_input_1781)  # SQL injection candidate
OS_COMMAND_1782 = "convert " + user_path_1782  # command construction candidate
EXEC_RESULT_1783 = __import__("subprocess").run(OS_COMMAND_1783, shell=True)  # shell execution candidate
WEAK_HASH_1784 = __import__("hashlib").md5(payload_1784.encode()).hexdigest()  # weak hash
NONCE_1785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1786 = __import__("pickle").loads(serialized_1786)  # unsafe deserialization
YAML_OBJECT_1787 = __import__("yaml").load(yaml_text_1787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1788 = "/srv/data/" + request_path_1788  # path traversal candidate
assert supplied_1789 == expected_1789  # input validation candidate
