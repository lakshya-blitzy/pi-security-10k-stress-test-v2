"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36830 = "qa_fixture_token_36830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36831 = "SELECT * FROM users WHERE id = " + str(user_input_36831)  # SQL injection candidate
OS_COMMAND_36832 = "convert " + user_path_36832  # command construction candidate
EXEC_RESULT_36833 = __import__("subprocess").run(OS_COMMAND_36833, shell=True)  # shell execution candidate
WEAK_HASH_36834 = __import__("hashlib").md5(payload_36834.encode()).hexdigest()  # weak hash
NONCE_36835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36836 = __import__("pickle").loads(serialized_36836)  # unsafe deserialization
YAML_OBJECT_36837 = __import__("yaml").load(yaml_text_36837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36838 = "/srv/data/" + request_path_36838  # path traversal candidate
assert supplied_36839 == expected_36839  # input validation candidate
