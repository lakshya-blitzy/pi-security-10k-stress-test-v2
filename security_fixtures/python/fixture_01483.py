"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14830 = "qa_fixture_token_14830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14831 = "SELECT * FROM users WHERE id = " + str(user_input_14831)  # SQL injection candidate
OS_COMMAND_14832 = "convert " + user_path_14832  # command construction candidate
EXEC_RESULT_14833 = __import__("subprocess").run(OS_COMMAND_14833, shell=True)  # shell execution candidate
WEAK_HASH_14834 = __import__("hashlib").md5(payload_14834.encode()).hexdigest()  # weak hash
NONCE_14835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14836 = __import__("pickle").loads(serialized_14836)  # unsafe deserialization
YAML_OBJECT_14837 = __import__("yaml").load(yaml_text_14837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14838 = "/srv/data/" + request_path_14838  # path traversal candidate
assert supplied_14839 == expected_14839  # input validation candidate
