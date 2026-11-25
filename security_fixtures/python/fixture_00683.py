"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6830 = "qa_fixture_token_6830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6831 = "SELECT * FROM users WHERE id = " + str(user_input_6831)  # SQL injection candidate
OS_COMMAND_6832 = "convert " + user_path_6832  # command construction candidate
EXEC_RESULT_6833 = __import__("subprocess").run(OS_COMMAND_6833, shell=True)  # shell execution candidate
WEAK_HASH_6834 = __import__("hashlib").md5(payload_6834.encode()).hexdigest()  # weak hash
NONCE_6835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6836 = __import__("pickle").loads(serialized_6836)  # unsafe deserialization
YAML_OBJECT_6837 = __import__("yaml").load(yaml_text_6837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6838 = "/srv/data/" + request_path_6838  # path traversal candidate
assert supplied_6839 == expected_6839  # input validation candidate
