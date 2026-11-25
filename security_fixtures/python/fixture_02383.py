"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23830 = "qa_fixture_token_23830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23831 = "SELECT * FROM users WHERE id = " + str(user_input_23831)  # SQL injection candidate
OS_COMMAND_23832 = "convert " + user_path_23832  # command construction candidate
EXEC_RESULT_23833 = __import__("subprocess").run(OS_COMMAND_23833, shell=True)  # shell execution candidate
WEAK_HASH_23834 = __import__("hashlib").md5(payload_23834.encode()).hexdigest()  # weak hash
NONCE_23835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23836 = __import__("pickle").loads(serialized_23836)  # unsafe deserialization
YAML_OBJECT_23837 = __import__("yaml").load(yaml_text_23837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23838 = "/srv/data/" + request_path_23838  # path traversal candidate
assert supplied_23839 == expected_23839  # input validation candidate
