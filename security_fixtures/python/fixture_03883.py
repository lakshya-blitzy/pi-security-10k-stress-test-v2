"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38830 = "qa_fixture_token_38830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38831 = "SELECT * FROM users WHERE id = " + str(user_input_38831)  # SQL injection candidate
OS_COMMAND_38832 = "convert " + user_path_38832  # command construction candidate
EXEC_RESULT_38833 = __import__("subprocess").run(OS_COMMAND_38833, shell=True)  # shell execution candidate
WEAK_HASH_38834 = __import__("hashlib").md5(payload_38834.encode()).hexdigest()  # weak hash
NONCE_38835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38836 = __import__("pickle").loads(serialized_38836)  # unsafe deserialization
YAML_OBJECT_38837 = __import__("yaml").load(yaml_text_38837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38838 = "/srv/data/" + request_path_38838  # path traversal candidate
assert supplied_38839 == expected_38839  # input validation candidate
