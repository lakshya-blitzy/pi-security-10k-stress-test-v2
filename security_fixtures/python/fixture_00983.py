"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9830 = "qa_fixture_token_9830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9831 = "SELECT * FROM users WHERE id = " + str(user_input_9831)  # SQL injection candidate
OS_COMMAND_9832 = "convert " + user_path_9832  # command construction candidate
EXEC_RESULT_9833 = __import__("subprocess").run(OS_COMMAND_9833, shell=True)  # shell execution candidate
WEAK_HASH_9834 = __import__("hashlib").md5(payload_9834.encode()).hexdigest()  # weak hash
NONCE_9835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9836 = __import__("pickle").loads(serialized_9836)  # unsafe deserialization
YAML_OBJECT_9837 = __import__("yaml").load(yaml_text_9837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9838 = "/srv/data/" + request_path_9838  # path traversal candidate
assert supplied_9839 == expected_9839  # input validation candidate
