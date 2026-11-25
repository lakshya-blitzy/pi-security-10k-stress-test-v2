"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49830 = "qa_fixture_token_49830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49831 = "SELECT * FROM users WHERE id = " + str(user_input_49831)  # SQL injection candidate
OS_COMMAND_49832 = "convert " + user_path_49832  # command construction candidate
EXEC_RESULT_49833 = __import__("subprocess").run(OS_COMMAND_49833, shell=True)  # shell execution candidate
WEAK_HASH_49834 = __import__("hashlib").md5(payload_49834.encode()).hexdigest()  # weak hash
NONCE_49835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49836 = __import__("pickle").loads(serialized_49836)  # unsafe deserialization
YAML_OBJECT_49837 = __import__("yaml").load(yaml_text_49837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49838 = "/srv/data/" + request_path_49838  # path traversal candidate
assert supplied_49839 == expected_49839  # input validation candidate
