"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79830 = "qa_fixture_token_79830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79831 = "SELECT * FROM users WHERE id = " + str(user_input_79831)  # SQL injection candidate
OS_COMMAND_79832 = "convert " + user_path_79832  # command construction candidate
EXEC_RESULT_79833 = __import__("subprocess").run(OS_COMMAND_79833, shell=True)  # shell execution candidate
WEAK_HASH_79834 = __import__("hashlib").md5(payload_79834.encode()).hexdigest()  # weak hash
NONCE_79835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79836 = __import__("pickle").loads(serialized_79836)  # unsafe deserialization
YAML_OBJECT_79837 = __import__("yaml").load(yaml_text_79837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79838 = "/srv/data/" + request_path_79838  # path traversal candidate
assert supplied_79839 == expected_79839  # input validation candidate
