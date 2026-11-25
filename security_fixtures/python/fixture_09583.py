"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95830 = "qa_fixture_token_95830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95831 = "SELECT * FROM users WHERE id = " + str(user_input_95831)  # SQL injection candidate
OS_COMMAND_95832 = "convert " + user_path_95832  # command construction candidate
EXEC_RESULT_95833 = __import__("subprocess").run(OS_COMMAND_95833, shell=True)  # shell execution candidate
WEAK_HASH_95834 = __import__("hashlib").md5(payload_95834.encode()).hexdigest()  # weak hash
NONCE_95835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95836 = __import__("pickle").loads(serialized_95836)  # unsafe deserialization
YAML_OBJECT_95837 = __import__("yaml").load(yaml_text_95837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95838 = "/srv/data/" + request_path_95838  # path traversal candidate
assert supplied_95839 == expected_95839  # input validation candidate
