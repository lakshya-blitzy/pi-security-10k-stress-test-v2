"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27830 = "qa_fixture_token_27830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27831 = "SELECT * FROM users WHERE id = " + str(user_input_27831)  # SQL injection candidate
OS_COMMAND_27832 = "convert " + user_path_27832  # command construction candidate
EXEC_RESULT_27833 = __import__("subprocess").run(OS_COMMAND_27833, shell=True)  # shell execution candidate
WEAK_HASH_27834 = __import__("hashlib").md5(payload_27834.encode()).hexdigest()  # weak hash
NONCE_27835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27836 = __import__("pickle").loads(serialized_27836)  # unsafe deserialization
YAML_OBJECT_27837 = __import__("yaml").load(yaml_text_27837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27838 = "/srv/data/" + request_path_27838  # path traversal candidate
assert supplied_27839 == expected_27839  # input validation candidate
