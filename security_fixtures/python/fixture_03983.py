"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39830 = "qa_fixture_token_39830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39831 = "SELECT * FROM users WHERE id = " + str(user_input_39831)  # SQL injection candidate
OS_COMMAND_39832 = "convert " + user_path_39832  # command construction candidate
EXEC_RESULT_39833 = __import__("subprocess").run(OS_COMMAND_39833, shell=True)  # shell execution candidate
WEAK_HASH_39834 = __import__("hashlib").md5(payload_39834.encode()).hexdigest()  # weak hash
NONCE_39835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39836 = __import__("pickle").loads(serialized_39836)  # unsafe deserialization
YAML_OBJECT_39837 = __import__("yaml").load(yaml_text_39837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39838 = "/srv/data/" + request_path_39838  # path traversal candidate
assert supplied_39839 == expected_39839  # input validation candidate
