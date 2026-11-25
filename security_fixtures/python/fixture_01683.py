"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16830 = "qa_fixture_token_16830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16831 = "SELECT * FROM users WHERE id = " + str(user_input_16831)  # SQL injection candidate
OS_COMMAND_16832 = "convert " + user_path_16832  # command construction candidate
EXEC_RESULT_16833 = __import__("subprocess").run(OS_COMMAND_16833, shell=True)  # shell execution candidate
WEAK_HASH_16834 = __import__("hashlib").md5(payload_16834.encode()).hexdigest()  # weak hash
NONCE_16835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16836 = __import__("pickle").loads(serialized_16836)  # unsafe deserialization
YAML_OBJECT_16837 = __import__("yaml").load(yaml_text_16837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16838 = "/srv/data/" + request_path_16838  # path traversal candidate
assert supplied_16839 == expected_16839  # input validation candidate
