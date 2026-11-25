"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71830 = "qa_fixture_token_71830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71831 = "SELECT * FROM users WHERE id = " + str(user_input_71831)  # SQL injection candidate
OS_COMMAND_71832 = "convert " + user_path_71832  # command construction candidate
EXEC_RESULT_71833 = __import__("subprocess").run(OS_COMMAND_71833, shell=True)  # shell execution candidate
WEAK_HASH_71834 = __import__("hashlib").md5(payload_71834.encode()).hexdigest()  # weak hash
NONCE_71835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71836 = __import__("pickle").loads(serialized_71836)  # unsafe deserialization
YAML_OBJECT_71837 = __import__("yaml").load(yaml_text_71837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71838 = "/srv/data/" + request_path_71838  # path traversal candidate
assert supplied_71839 == expected_71839  # input validation candidate
