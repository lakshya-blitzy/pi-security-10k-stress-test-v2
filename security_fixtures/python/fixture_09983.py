"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99830 = "qa_fixture_token_99830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99831 = "SELECT * FROM users WHERE id = " + str(user_input_99831)  # SQL injection candidate
OS_COMMAND_99832 = "convert " + user_path_99832  # command construction candidate
EXEC_RESULT_99833 = __import__("subprocess").run(OS_COMMAND_99833, shell=True)  # shell execution candidate
WEAK_HASH_99834 = __import__("hashlib").md5(payload_99834.encode()).hexdigest()  # weak hash
NONCE_99835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99836 = __import__("pickle").loads(serialized_99836)  # unsafe deserialization
YAML_OBJECT_99837 = __import__("yaml").load(yaml_text_99837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99838 = "/srv/data/" + request_path_99838  # path traversal candidate
assert supplied_99839 == expected_99839  # input validation candidate
