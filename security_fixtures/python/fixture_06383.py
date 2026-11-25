"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63830 = "qa_fixture_token_63830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63831 = "SELECT * FROM users WHERE id = " + str(user_input_63831)  # SQL injection candidate
OS_COMMAND_63832 = "convert " + user_path_63832  # command construction candidate
EXEC_RESULT_63833 = __import__("subprocess").run(OS_COMMAND_63833, shell=True)  # shell execution candidate
WEAK_HASH_63834 = __import__("hashlib").md5(payload_63834.encode()).hexdigest()  # weak hash
NONCE_63835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63836 = __import__("pickle").loads(serialized_63836)  # unsafe deserialization
YAML_OBJECT_63837 = __import__("yaml").load(yaml_text_63837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63838 = "/srv/data/" + request_path_63838  # path traversal candidate
assert supplied_63839 == expected_63839  # input validation candidate
