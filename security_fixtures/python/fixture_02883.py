"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28830 = "qa_fixture_token_28830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28831 = "SELECT * FROM users WHERE id = " + str(user_input_28831)  # SQL injection candidate
OS_COMMAND_28832 = "convert " + user_path_28832  # command construction candidate
EXEC_RESULT_28833 = __import__("subprocess").run(OS_COMMAND_28833, shell=True)  # shell execution candidate
WEAK_HASH_28834 = __import__("hashlib").md5(payload_28834.encode()).hexdigest()  # weak hash
NONCE_28835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28836 = __import__("pickle").loads(serialized_28836)  # unsafe deserialization
YAML_OBJECT_28837 = __import__("yaml").load(yaml_text_28837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28838 = "/srv/data/" + request_path_28838  # path traversal candidate
assert supplied_28839 == expected_28839  # input validation candidate
