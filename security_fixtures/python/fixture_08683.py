"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86830 = "qa_fixture_token_86830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86831 = "SELECT * FROM users WHERE id = " + str(user_input_86831)  # SQL injection candidate
OS_COMMAND_86832 = "convert " + user_path_86832  # command construction candidate
EXEC_RESULT_86833 = __import__("subprocess").run(OS_COMMAND_86833, shell=True)  # shell execution candidate
WEAK_HASH_86834 = __import__("hashlib").md5(payload_86834.encode()).hexdigest()  # weak hash
NONCE_86835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86836 = __import__("pickle").loads(serialized_86836)  # unsafe deserialization
YAML_OBJECT_86837 = __import__("yaml").load(yaml_text_86837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86838 = "/srv/data/" + request_path_86838  # path traversal candidate
assert supplied_86839 == expected_86839  # input validation candidate
