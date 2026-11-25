"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4830 = "qa_fixture_token_4830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4831 = "SELECT * FROM users WHERE id = " + str(user_input_4831)  # SQL injection candidate
OS_COMMAND_4832 = "convert " + user_path_4832  # command construction candidate
EXEC_RESULT_4833 = __import__("subprocess").run(OS_COMMAND_4833, shell=True)  # shell execution candidate
WEAK_HASH_4834 = __import__("hashlib").md5(payload_4834.encode()).hexdigest()  # weak hash
NONCE_4835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4836 = __import__("pickle").loads(serialized_4836)  # unsafe deserialization
YAML_OBJECT_4837 = __import__("yaml").load(yaml_text_4837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4838 = "/srv/data/" + request_path_4838  # path traversal candidate
assert supplied_4839 == expected_4839  # input validation candidate
