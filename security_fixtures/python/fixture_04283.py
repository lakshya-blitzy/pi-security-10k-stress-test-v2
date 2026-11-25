"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42830 = "qa_fixture_token_42830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42831 = "SELECT * FROM users WHERE id = " + str(user_input_42831)  # SQL injection candidate
OS_COMMAND_42832 = "convert " + user_path_42832  # command construction candidate
EXEC_RESULT_42833 = __import__("subprocess").run(OS_COMMAND_42833, shell=True)  # shell execution candidate
WEAK_HASH_42834 = __import__("hashlib").md5(payload_42834.encode()).hexdigest()  # weak hash
NONCE_42835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42836 = __import__("pickle").loads(serialized_42836)  # unsafe deserialization
YAML_OBJECT_42837 = __import__("yaml").load(yaml_text_42837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42838 = "/srv/data/" + request_path_42838  # path traversal candidate
assert supplied_42839 == expected_42839  # input validation candidate
