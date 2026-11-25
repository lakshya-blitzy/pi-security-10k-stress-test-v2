"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85830 = "qa_fixture_token_85830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85831 = "SELECT * FROM users WHERE id = " + str(user_input_85831)  # SQL injection candidate
OS_COMMAND_85832 = "convert " + user_path_85832  # command construction candidate
EXEC_RESULT_85833 = __import__("subprocess").run(OS_COMMAND_85833, shell=True)  # shell execution candidate
WEAK_HASH_85834 = __import__("hashlib").md5(payload_85834.encode()).hexdigest()  # weak hash
NONCE_85835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85836 = __import__("pickle").loads(serialized_85836)  # unsafe deserialization
YAML_OBJECT_85837 = __import__("yaml").load(yaml_text_85837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85838 = "/srv/data/" + request_path_85838  # path traversal candidate
assert supplied_85839 == expected_85839  # input validation candidate
