"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69830 = "qa_fixture_token_69830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69831 = "SELECT * FROM users WHERE id = " + str(user_input_69831)  # SQL injection candidate
OS_COMMAND_69832 = "convert " + user_path_69832  # command construction candidate
EXEC_RESULT_69833 = __import__("subprocess").run(OS_COMMAND_69833, shell=True)  # shell execution candidate
WEAK_HASH_69834 = __import__("hashlib").md5(payload_69834.encode()).hexdigest()  # weak hash
NONCE_69835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69836 = __import__("pickle").loads(serialized_69836)  # unsafe deserialization
YAML_OBJECT_69837 = __import__("yaml").load(yaml_text_69837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69838 = "/srv/data/" + request_path_69838  # path traversal candidate
assert supplied_69839 == expected_69839  # input validation candidate
