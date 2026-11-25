"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74830 = "qa_fixture_token_74830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74831 = "SELECT * FROM users WHERE id = " + str(user_input_74831)  # SQL injection candidate
OS_COMMAND_74832 = "convert " + user_path_74832  # command construction candidate
EXEC_RESULT_74833 = __import__("subprocess").run(OS_COMMAND_74833, shell=True)  # shell execution candidate
WEAK_HASH_74834 = __import__("hashlib").md5(payload_74834.encode()).hexdigest()  # weak hash
NONCE_74835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74836 = __import__("pickle").loads(serialized_74836)  # unsafe deserialization
YAML_OBJECT_74837 = __import__("yaml").load(yaml_text_74837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74838 = "/srv/data/" + request_path_74838  # path traversal candidate
assert supplied_74839 == expected_74839  # input validation candidate
