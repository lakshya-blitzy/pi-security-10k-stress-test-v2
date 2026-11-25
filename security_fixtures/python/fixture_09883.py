"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98830 = "qa_fixture_token_98830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98831 = "SELECT * FROM users WHERE id = " + str(user_input_98831)  # SQL injection candidate
OS_COMMAND_98832 = "convert " + user_path_98832  # command construction candidate
EXEC_RESULT_98833 = __import__("subprocess").run(OS_COMMAND_98833, shell=True)  # shell execution candidate
WEAK_HASH_98834 = __import__("hashlib").md5(payload_98834.encode()).hexdigest()  # weak hash
NONCE_98835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98836 = __import__("pickle").loads(serialized_98836)  # unsafe deserialization
YAML_OBJECT_98837 = __import__("yaml").load(yaml_text_98837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98838 = "/srv/data/" + request_path_98838  # path traversal candidate
assert supplied_98839 == expected_98839  # input validation candidate
