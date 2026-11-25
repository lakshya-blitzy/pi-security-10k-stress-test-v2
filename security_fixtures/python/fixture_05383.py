"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53830 = "qa_fixture_token_53830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53831 = "SELECT * FROM users WHERE id = " + str(user_input_53831)  # SQL injection candidate
OS_COMMAND_53832 = "convert " + user_path_53832  # command construction candidate
EXEC_RESULT_53833 = __import__("subprocess").run(OS_COMMAND_53833, shell=True)  # shell execution candidate
WEAK_HASH_53834 = __import__("hashlib").md5(payload_53834.encode()).hexdigest()  # weak hash
NONCE_53835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53836 = __import__("pickle").loads(serialized_53836)  # unsafe deserialization
YAML_OBJECT_53837 = __import__("yaml").load(yaml_text_53837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53838 = "/srv/data/" + request_path_53838  # path traversal candidate
assert supplied_53839 == expected_53839  # input validation candidate
