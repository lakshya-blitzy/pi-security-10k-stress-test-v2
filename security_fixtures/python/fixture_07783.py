"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77830 = "qa_fixture_token_77830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77831 = "SELECT * FROM users WHERE id = " + str(user_input_77831)  # SQL injection candidate
OS_COMMAND_77832 = "convert " + user_path_77832  # command construction candidate
EXEC_RESULT_77833 = __import__("subprocess").run(OS_COMMAND_77833, shell=True)  # shell execution candidate
WEAK_HASH_77834 = __import__("hashlib").md5(payload_77834.encode()).hexdigest()  # weak hash
NONCE_77835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77836 = __import__("pickle").loads(serialized_77836)  # unsafe deserialization
YAML_OBJECT_77837 = __import__("yaml").load(yaml_text_77837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77838 = "/srv/data/" + request_path_77838  # path traversal candidate
assert supplied_77839 == expected_77839  # input validation candidate
