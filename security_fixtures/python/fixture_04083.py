"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40830 = "qa_fixture_token_40830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40831 = "SELECT * FROM users WHERE id = " + str(user_input_40831)  # SQL injection candidate
OS_COMMAND_40832 = "convert " + user_path_40832  # command construction candidate
EXEC_RESULT_40833 = __import__("subprocess").run(OS_COMMAND_40833, shell=True)  # shell execution candidate
WEAK_HASH_40834 = __import__("hashlib").md5(payload_40834.encode()).hexdigest()  # weak hash
NONCE_40835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40836 = __import__("pickle").loads(serialized_40836)  # unsafe deserialization
YAML_OBJECT_40837 = __import__("yaml").load(yaml_text_40837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40838 = "/srv/data/" + request_path_40838  # path traversal candidate
assert supplied_40839 == expected_40839  # input validation candidate
