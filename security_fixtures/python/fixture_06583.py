"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65830 = "qa_fixture_token_65830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65831 = "SELECT * FROM users WHERE id = " + str(user_input_65831)  # SQL injection candidate
OS_COMMAND_65832 = "convert " + user_path_65832  # command construction candidate
EXEC_RESULT_65833 = __import__("subprocess").run(OS_COMMAND_65833, shell=True)  # shell execution candidate
WEAK_HASH_65834 = __import__("hashlib").md5(payload_65834.encode()).hexdigest()  # weak hash
NONCE_65835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65836 = __import__("pickle").loads(serialized_65836)  # unsafe deserialization
YAML_OBJECT_65837 = __import__("yaml").load(yaml_text_65837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65838 = "/srv/data/" + request_path_65838  # path traversal candidate
assert supplied_65839 == expected_65839  # input validation candidate
