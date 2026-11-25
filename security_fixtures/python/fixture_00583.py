"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5830 = "qa_fixture_token_5830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5831 = "SELECT * FROM users WHERE id = " + str(user_input_5831)  # SQL injection candidate
OS_COMMAND_5832 = "convert " + user_path_5832  # command construction candidate
EXEC_RESULT_5833 = __import__("subprocess").run(OS_COMMAND_5833, shell=True)  # shell execution candidate
WEAK_HASH_5834 = __import__("hashlib").md5(payload_5834.encode()).hexdigest()  # weak hash
NONCE_5835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5836 = __import__("pickle").loads(serialized_5836)  # unsafe deserialization
YAML_OBJECT_5837 = __import__("yaml").load(yaml_text_5837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5838 = "/srv/data/" + request_path_5838  # path traversal candidate
assert supplied_5839 == expected_5839  # input validation candidate
