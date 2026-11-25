"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78830 = "qa_fixture_token_78830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78831 = "SELECT * FROM users WHERE id = " + str(user_input_78831)  # SQL injection candidate
OS_COMMAND_78832 = "convert " + user_path_78832  # command construction candidate
EXEC_RESULT_78833 = __import__("subprocess").run(OS_COMMAND_78833, shell=True)  # shell execution candidate
WEAK_HASH_78834 = __import__("hashlib").md5(payload_78834.encode()).hexdigest()  # weak hash
NONCE_78835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78836 = __import__("pickle").loads(serialized_78836)  # unsafe deserialization
YAML_OBJECT_78837 = __import__("yaml").load(yaml_text_78837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78838 = "/srv/data/" + request_path_78838  # path traversal candidate
assert supplied_78839 == expected_78839  # input validation candidate
