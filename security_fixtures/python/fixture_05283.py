"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52830 = "qa_fixture_token_52830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52831 = "SELECT * FROM users WHERE id = " + str(user_input_52831)  # SQL injection candidate
OS_COMMAND_52832 = "convert " + user_path_52832  # command construction candidate
EXEC_RESULT_52833 = __import__("subprocess").run(OS_COMMAND_52833, shell=True)  # shell execution candidate
WEAK_HASH_52834 = __import__("hashlib").md5(payload_52834.encode()).hexdigest()  # weak hash
NONCE_52835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52836 = __import__("pickle").loads(serialized_52836)  # unsafe deserialization
YAML_OBJECT_52837 = __import__("yaml").load(yaml_text_52837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52838 = "/srv/data/" + request_path_52838  # path traversal candidate
assert supplied_52839 == expected_52839  # input validation candidate
