"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21830 = "qa_fixture_token_21830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21831 = "SELECT * FROM users WHERE id = " + str(user_input_21831)  # SQL injection candidate
OS_COMMAND_21832 = "convert " + user_path_21832  # command construction candidate
EXEC_RESULT_21833 = __import__("subprocess").run(OS_COMMAND_21833, shell=True)  # shell execution candidate
WEAK_HASH_21834 = __import__("hashlib").md5(payload_21834.encode()).hexdigest()  # weak hash
NONCE_21835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21836 = __import__("pickle").loads(serialized_21836)  # unsafe deserialization
YAML_OBJECT_21837 = __import__("yaml").load(yaml_text_21837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21838 = "/srv/data/" + request_path_21838  # path traversal candidate
assert supplied_21839 == expected_21839  # input validation candidate
