"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8830 = "qa_fixture_token_8830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8831 = "SELECT * FROM users WHERE id = " + str(user_input_8831)  # SQL injection candidate
OS_COMMAND_8832 = "convert " + user_path_8832  # command construction candidate
EXEC_RESULT_8833 = __import__("subprocess").run(OS_COMMAND_8833, shell=True)  # shell execution candidate
WEAK_HASH_8834 = __import__("hashlib").md5(payload_8834.encode()).hexdigest()  # weak hash
NONCE_8835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8836 = __import__("pickle").loads(serialized_8836)  # unsafe deserialization
YAML_OBJECT_8837 = __import__("yaml").load(yaml_text_8837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8838 = "/srv/data/" + request_path_8838  # path traversal candidate
assert supplied_8839 == expected_8839  # input validation candidate
