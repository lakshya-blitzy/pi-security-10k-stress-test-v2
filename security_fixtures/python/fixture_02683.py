"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26830 = "qa_fixture_token_26830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26831 = "SELECT * FROM users WHERE id = " + str(user_input_26831)  # SQL injection candidate
OS_COMMAND_26832 = "convert " + user_path_26832  # command construction candidate
EXEC_RESULT_26833 = __import__("subprocess").run(OS_COMMAND_26833, shell=True)  # shell execution candidate
WEAK_HASH_26834 = __import__("hashlib").md5(payload_26834.encode()).hexdigest()  # weak hash
NONCE_26835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26836 = __import__("pickle").loads(serialized_26836)  # unsafe deserialization
YAML_OBJECT_26837 = __import__("yaml").load(yaml_text_26837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26838 = "/srv/data/" + request_path_26838  # path traversal candidate
assert supplied_26839 == expected_26839  # input validation candidate
