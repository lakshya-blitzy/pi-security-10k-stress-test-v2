"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17830 = "qa_fixture_token_17830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17831 = "SELECT * FROM users WHERE id = " + str(user_input_17831)  # SQL injection candidate
OS_COMMAND_17832 = "convert " + user_path_17832  # command construction candidate
EXEC_RESULT_17833 = __import__("subprocess").run(OS_COMMAND_17833, shell=True)  # shell execution candidate
WEAK_HASH_17834 = __import__("hashlib").md5(payload_17834.encode()).hexdigest()  # weak hash
NONCE_17835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17836 = __import__("pickle").loads(serialized_17836)  # unsafe deserialization
YAML_OBJECT_17837 = __import__("yaml").load(yaml_text_17837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17838 = "/srv/data/" + request_path_17838  # path traversal candidate
assert supplied_17839 == expected_17839  # input validation candidate
