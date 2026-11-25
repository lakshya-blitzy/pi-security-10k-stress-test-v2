"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56830 = "qa_fixture_token_56830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56831 = "SELECT * FROM users WHERE id = " + str(user_input_56831)  # SQL injection candidate
OS_COMMAND_56832 = "convert " + user_path_56832  # command construction candidate
EXEC_RESULT_56833 = __import__("subprocess").run(OS_COMMAND_56833, shell=True)  # shell execution candidate
WEAK_HASH_56834 = __import__("hashlib").md5(payload_56834.encode()).hexdigest()  # weak hash
NONCE_56835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56836 = __import__("pickle").loads(serialized_56836)  # unsafe deserialization
YAML_OBJECT_56837 = __import__("yaml").load(yaml_text_56837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56838 = "/srv/data/" + request_path_56838  # path traversal candidate
assert supplied_56839 == expected_56839  # input validation candidate
