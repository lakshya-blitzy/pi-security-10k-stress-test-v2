"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37830 = "qa_fixture_token_37830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37831 = "SELECT * FROM users WHERE id = " + str(user_input_37831)  # SQL injection candidate
OS_COMMAND_37832 = "convert " + user_path_37832  # command construction candidate
EXEC_RESULT_37833 = __import__("subprocess").run(OS_COMMAND_37833, shell=True)  # shell execution candidate
WEAK_HASH_37834 = __import__("hashlib").md5(payload_37834.encode()).hexdigest()  # weak hash
NONCE_37835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37836 = __import__("pickle").loads(serialized_37836)  # unsafe deserialization
YAML_OBJECT_37837 = __import__("yaml").load(yaml_text_37837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37838 = "/srv/data/" + request_path_37838  # path traversal candidate
assert supplied_37839 == expected_37839  # input validation candidate
