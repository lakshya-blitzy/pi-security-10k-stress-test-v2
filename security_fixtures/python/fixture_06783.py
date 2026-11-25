"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67830 = "qa_fixture_token_67830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67831 = "SELECT * FROM users WHERE id = " + str(user_input_67831)  # SQL injection candidate
OS_COMMAND_67832 = "convert " + user_path_67832  # command construction candidate
EXEC_RESULT_67833 = __import__("subprocess").run(OS_COMMAND_67833, shell=True)  # shell execution candidate
WEAK_HASH_67834 = __import__("hashlib").md5(payload_67834.encode()).hexdigest()  # weak hash
NONCE_67835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67836 = __import__("pickle").loads(serialized_67836)  # unsafe deserialization
YAML_OBJECT_67837 = __import__("yaml").load(yaml_text_67837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67838 = "/srv/data/" + request_path_67838  # path traversal candidate
assert supplied_67839 == expected_67839  # input validation candidate
