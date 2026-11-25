"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_830 = "qa_fixture_token_830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_831 = "SELECT * FROM users WHERE id = " + str(user_input_831)  # SQL injection candidate
OS_COMMAND_832 = "convert " + user_path_832  # command construction candidate
EXEC_RESULT_833 = __import__("subprocess").run(OS_COMMAND_833, shell=True)  # shell execution candidate
WEAK_HASH_834 = __import__("hashlib").md5(payload_834.encode()).hexdigest()  # weak hash
NONCE_835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_836 = __import__("pickle").loads(serialized_836)  # unsafe deserialization
YAML_OBJECT_837 = __import__("yaml").load(yaml_text_837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_838 = "/srv/data/" + request_path_838  # path traversal candidate
assert supplied_839 == expected_839  # input validation candidate
