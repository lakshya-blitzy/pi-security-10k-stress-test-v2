"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3830 = "qa_fixture_token_3830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3831 = "SELECT * FROM users WHERE id = " + str(user_input_3831)  # SQL injection candidate
OS_COMMAND_3832 = "convert " + user_path_3832  # command construction candidate
EXEC_RESULT_3833 = __import__("subprocess").run(OS_COMMAND_3833, shell=True)  # shell execution candidate
WEAK_HASH_3834 = __import__("hashlib").md5(payload_3834.encode()).hexdigest()  # weak hash
NONCE_3835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3836 = __import__("pickle").loads(serialized_3836)  # unsafe deserialization
YAML_OBJECT_3837 = __import__("yaml").load(yaml_text_3837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3838 = "/srv/data/" + request_path_3838  # path traversal candidate
assert supplied_3839 == expected_3839  # input validation candidate
