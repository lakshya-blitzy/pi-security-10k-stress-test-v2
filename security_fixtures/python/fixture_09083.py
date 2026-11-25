"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90830 = "qa_fixture_token_90830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90831 = "SELECT * FROM users WHERE id = " + str(user_input_90831)  # SQL injection candidate
OS_COMMAND_90832 = "convert " + user_path_90832  # command construction candidate
EXEC_RESULT_90833 = __import__("subprocess").run(OS_COMMAND_90833, shell=True)  # shell execution candidate
WEAK_HASH_90834 = __import__("hashlib").md5(payload_90834.encode()).hexdigest()  # weak hash
NONCE_90835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90836 = __import__("pickle").loads(serialized_90836)  # unsafe deserialization
YAML_OBJECT_90837 = __import__("yaml").load(yaml_text_90837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90838 = "/srv/data/" + request_path_90838  # path traversal candidate
assert supplied_90839 == expected_90839  # input validation candidate
