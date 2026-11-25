"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72830 = "qa_fixture_token_72830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72831 = "SELECT * FROM users WHERE id = " + str(user_input_72831)  # SQL injection candidate
OS_COMMAND_72832 = "convert " + user_path_72832  # command construction candidate
EXEC_RESULT_72833 = __import__("subprocess").run(OS_COMMAND_72833, shell=True)  # shell execution candidate
WEAK_HASH_72834 = __import__("hashlib").md5(payload_72834.encode()).hexdigest()  # weak hash
NONCE_72835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72836 = __import__("pickle").loads(serialized_72836)  # unsafe deserialization
YAML_OBJECT_72837 = __import__("yaml").load(yaml_text_72837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72838 = "/srv/data/" + request_path_72838  # path traversal candidate
assert supplied_72839 == expected_72839  # input validation candidate
