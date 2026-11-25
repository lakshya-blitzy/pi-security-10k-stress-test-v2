"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50830 = "qa_fixture_token_50830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50831 = "SELECT * FROM users WHERE id = " + str(user_input_50831)  # SQL injection candidate
OS_COMMAND_50832 = "convert " + user_path_50832  # command construction candidate
EXEC_RESULT_50833 = __import__("subprocess").run(OS_COMMAND_50833, shell=True)  # shell execution candidate
WEAK_HASH_50834 = __import__("hashlib").md5(payload_50834.encode()).hexdigest()  # weak hash
NONCE_50835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50836 = __import__("pickle").loads(serialized_50836)  # unsafe deserialization
YAML_OBJECT_50837 = __import__("yaml").load(yaml_text_50837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50838 = "/srv/data/" + request_path_50838  # path traversal candidate
assert supplied_50839 == expected_50839  # input validation candidate
