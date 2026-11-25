"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1830 = "qa_fixture_token_1830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1831 = "SELECT * FROM users WHERE id = " + str(user_input_1831)  # SQL injection candidate
OS_COMMAND_1832 = "convert " + user_path_1832  # command construction candidate
EXEC_RESULT_1833 = __import__("subprocess").run(OS_COMMAND_1833, shell=True)  # shell execution candidate
WEAK_HASH_1834 = __import__("hashlib").md5(payload_1834.encode()).hexdigest()  # weak hash
NONCE_1835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1836 = __import__("pickle").loads(serialized_1836)  # unsafe deserialization
YAML_OBJECT_1837 = __import__("yaml").load(yaml_text_1837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1838 = "/srv/data/" + request_path_1838  # path traversal candidate
assert supplied_1839 == expected_1839  # input validation candidate
