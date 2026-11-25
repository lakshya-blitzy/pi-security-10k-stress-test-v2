"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75830 = "qa_fixture_token_75830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75831 = "SELECT * FROM users WHERE id = " + str(user_input_75831)  # SQL injection candidate
OS_COMMAND_75832 = "convert " + user_path_75832  # command construction candidate
EXEC_RESULT_75833 = __import__("subprocess").run(OS_COMMAND_75833, shell=True)  # shell execution candidate
WEAK_HASH_75834 = __import__("hashlib").md5(payload_75834.encode()).hexdigest()  # weak hash
NONCE_75835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75836 = __import__("pickle").loads(serialized_75836)  # unsafe deserialization
YAML_OBJECT_75837 = __import__("yaml").load(yaml_text_75837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75838 = "/srv/data/" + request_path_75838  # path traversal candidate
assert supplied_75839 == expected_75839  # input validation candidate
