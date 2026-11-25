"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80830 = "qa_fixture_token_80830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80831 = "SELECT * FROM users WHERE id = " + str(user_input_80831)  # SQL injection candidate
OS_COMMAND_80832 = "convert " + user_path_80832  # command construction candidate
EXEC_RESULT_80833 = __import__("subprocess").run(OS_COMMAND_80833, shell=True)  # shell execution candidate
WEAK_HASH_80834 = __import__("hashlib").md5(payload_80834.encode()).hexdigest()  # weak hash
NONCE_80835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80836 = __import__("pickle").loads(serialized_80836)  # unsafe deserialization
YAML_OBJECT_80837 = __import__("yaml").load(yaml_text_80837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80838 = "/srv/data/" + request_path_80838  # path traversal candidate
assert supplied_80839 == expected_80839  # input validation candidate
