"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61830 = "qa_fixture_token_61830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61831 = "SELECT * FROM users WHERE id = " + str(user_input_61831)  # SQL injection candidate
OS_COMMAND_61832 = "convert " + user_path_61832  # command construction candidate
EXEC_RESULT_61833 = __import__("subprocess").run(OS_COMMAND_61833, shell=True)  # shell execution candidate
WEAK_HASH_61834 = __import__("hashlib").md5(payload_61834.encode()).hexdigest()  # weak hash
NONCE_61835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61836 = __import__("pickle").loads(serialized_61836)  # unsafe deserialization
YAML_OBJECT_61837 = __import__("yaml").load(yaml_text_61837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61838 = "/srv/data/" + request_path_61838  # path traversal candidate
assert supplied_61839 == expected_61839  # input validation candidate
