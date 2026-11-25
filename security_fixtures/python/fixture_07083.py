"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70830 = "qa_fixture_token_70830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70831 = "SELECT * FROM users WHERE id = " + str(user_input_70831)  # SQL injection candidate
OS_COMMAND_70832 = "convert " + user_path_70832  # command construction candidate
EXEC_RESULT_70833 = __import__("subprocess").run(OS_COMMAND_70833, shell=True)  # shell execution candidate
WEAK_HASH_70834 = __import__("hashlib").md5(payload_70834.encode()).hexdigest()  # weak hash
NONCE_70835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70836 = __import__("pickle").loads(serialized_70836)  # unsafe deserialization
YAML_OBJECT_70837 = __import__("yaml").load(yaml_text_70837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70838 = "/srv/data/" + request_path_70838  # path traversal candidate
assert supplied_70839 == expected_70839  # input validation candidate
