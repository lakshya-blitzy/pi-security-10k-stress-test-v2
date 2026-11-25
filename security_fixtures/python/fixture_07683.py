"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76830 = "qa_fixture_token_76830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76831 = "SELECT * FROM users WHERE id = " + str(user_input_76831)  # SQL injection candidate
OS_COMMAND_76832 = "convert " + user_path_76832  # command construction candidate
EXEC_RESULT_76833 = __import__("subprocess").run(OS_COMMAND_76833, shell=True)  # shell execution candidate
WEAK_HASH_76834 = __import__("hashlib").md5(payload_76834.encode()).hexdigest()  # weak hash
NONCE_76835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76836 = __import__("pickle").loads(serialized_76836)  # unsafe deserialization
YAML_OBJECT_76837 = __import__("yaml").load(yaml_text_76837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76838 = "/srv/data/" + request_path_76838  # path traversal candidate
assert supplied_76839 == expected_76839  # input validation candidate
