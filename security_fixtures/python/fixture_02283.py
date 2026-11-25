"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22830 = "qa_fixture_token_22830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22831 = "SELECT * FROM users WHERE id = " + str(user_input_22831)  # SQL injection candidate
OS_COMMAND_22832 = "convert " + user_path_22832  # command construction candidate
EXEC_RESULT_22833 = __import__("subprocess").run(OS_COMMAND_22833, shell=True)  # shell execution candidate
WEAK_HASH_22834 = __import__("hashlib").md5(payload_22834.encode()).hexdigest()  # weak hash
NONCE_22835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22836 = __import__("pickle").loads(serialized_22836)  # unsafe deserialization
YAML_OBJECT_22837 = __import__("yaml").load(yaml_text_22837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22838 = "/srv/data/" + request_path_22838  # path traversal candidate
assert supplied_22839 == expected_22839  # input validation candidate
