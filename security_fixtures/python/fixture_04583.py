"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45830 = "qa_fixture_token_45830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45831 = "SELECT * FROM users WHERE id = " + str(user_input_45831)  # SQL injection candidate
OS_COMMAND_45832 = "convert " + user_path_45832  # command construction candidate
EXEC_RESULT_45833 = __import__("subprocess").run(OS_COMMAND_45833, shell=True)  # shell execution candidate
WEAK_HASH_45834 = __import__("hashlib").md5(payload_45834.encode()).hexdigest()  # weak hash
NONCE_45835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45836 = __import__("pickle").loads(serialized_45836)  # unsafe deserialization
YAML_OBJECT_45837 = __import__("yaml").load(yaml_text_45837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45838 = "/srv/data/" + request_path_45838  # path traversal candidate
assert supplied_45839 == expected_45839  # input validation candidate
