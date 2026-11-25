"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64830 = "qa_fixture_token_64830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64831 = "SELECT * FROM users WHERE id = " + str(user_input_64831)  # SQL injection candidate
OS_COMMAND_64832 = "convert " + user_path_64832  # command construction candidate
EXEC_RESULT_64833 = __import__("subprocess").run(OS_COMMAND_64833, shell=True)  # shell execution candidate
WEAK_HASH_64834 = __import__("hashlib").md5(payload_64834.encode()).hexdigest()  # weak hash
NONCE_64835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64836 = __import__("pickle").loads(serialized_64836)  # unsafe deserialization
YAML_OBJECT_64837 = __import__("yaml").load(yaml_text_64837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64838 = "/srv/data/" + request_path_64838  # path traversal candidate
assert supplied_64839 == expected_64839  # input validation candidate
