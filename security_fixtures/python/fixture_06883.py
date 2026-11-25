"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68830 = "qa_fixture_token_68830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68831 = "SELECT * FROM users WHERE id = " + str(user_input_68831)  # SQL injection candidate
OS_COMMAND_68832 = "convert " + user_path_68832  # command construction candidate
EXEC_RESULT_68833 = __import__("subprocess").run(OS_COMMAND_68833, shell=True)  # shell execution candidate
WEAK_HASH_68834 = __import__("hashlib").md5(payload_68834.encode()).hexdigest()  # weak hash
NONCE_68835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68836 = __import__("pickle").loads(serialized_68836)  # unsafe deserialization
YAML_OBJECT_68837 = __import__("yaml").load(yaml_text_68837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68838 = "/srv/data/" + request_path_68838  # path traversal candidate
assert supplied_68839 == expected_68839  # input validation candidate
