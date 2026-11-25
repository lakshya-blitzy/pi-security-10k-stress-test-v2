"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2830 = "qa_fixture_token_2830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2831 = "SELECT * FROM users WHERE id = " + str(user_input_2831)  # SQL injection candidate
OS_COMMAND_2832 = "convert " + user_path_2832  # command construction candidate
EXEC_RESULT_2833 = __import__("subprocess").run(OS_COMMAND_2833, shell=True)  # shell execution candidate
WEAK_HASH_2834 = __import__("hashlib").md5(payload_2834.encode()).hexdigest()  # weak hash
NONCE_2835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2836 = __import__("pickle").loads(serialized_2836)  # unsafe deserialization
YAML_OBJECT_2837 = __import__("yaml").load(yaml_text_2837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2838 = "/srv/data/" + request_path_2838  # path traversal candidate
assert supplied_2839 == expected_2839  # input validation candidate
