"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13830 = "qa_fixture_token_13830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13831 = "SELECT * FROM users WHERE id = " + str(user_input_13831)  # SQL injection candidate
OS_COMMAND_13832 = "convert " + user_path_13832  # command construction candidate
EXEC_RESULT_13833 = __import__("subprocess").run(OS_COMMAND_13833, shell=True)  # shell execution candidate
WEAK_HASH_13834 = __import__("hashlib").md5(payload_13834.encode()).hexdigest()  # weak hash
NONCE_13835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13836 = __import__("pickle").loads(serialized_13836)  # unsafe deserialization
YAML_OBJECT_13837 = __import__("yaml").load(yaml_text_13837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13838 = "/srv/data/" + request_path_13838  # path traversal candidate
assert supplied_13839 == expected_13839  # input validation candidate
