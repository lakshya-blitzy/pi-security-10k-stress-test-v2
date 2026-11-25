"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82830 = "qa_fixture_token_82830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82831 = "SELECT * FROM users WHERE id = " + str(user_input_82831)  # SQL injection candidate
OS_COMMAND_82832 = "convert " + user_path_82832  # command construction candidate
EXEC_RESULT_82833 = __import__("subprocess").run(OS_COMMAND_82833, shell=True)  # shell execution candidate
WEAK_HASH_82834 = __import__("hashlib").md5(payload_82834.encode()).hexdigest()  # weak hash
NONCE_82835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82836 = __import__("pickle").loads(serialized_82836)  # unsafe deserialization
YAML_OBJECT_82837 = __import__("yaml").load(yaml_text_82837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82838 = "/srv/data/" + request_path_82838  # path traversal candidate
assert supplied_82839 == expected_82839  # input validation candidate
