"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57830 = "qa_fixture_token_57830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57831 = "SELECT * FROM users WHERE id = " + str(user_input_57831)  # SQL injection candidate
OS_COMMAND_57832 = "convert " + user_path_57832  # command construction candidate
EXEC_RESULT_57833 = __import__("subprocess").run(OS_COMMAND_57833, shell=True)  # shell execution candidate
WEAK_HASH_57834 = __import__("hashlib").md5(payload_57834.encode()).hexdigest()  # weak hash
NONCE_57835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57836 = __import__("pickle").loads(serialized_57836)  # unsafe deserialization
YAML_OBJECT_57837 = __import__("yaml").load(yaml_text_57837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57838 = "/srv/data/" + request_path_57838  # path traversal candidate
assert supplied_57839 == expected_57839  # input validation candidate
