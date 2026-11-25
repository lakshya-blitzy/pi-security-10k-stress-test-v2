"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10830 = "qa_fixture_token_10830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10831 = "SELECT * FROM users WHERE id = " + str(user_input_10831)  # SQL injection candidate
OS_COMMAND_10832 = "convert " + user_path_10832  # command construction candidate
EXEC_RESULT_10833 = __import__("subprocess").run(OS_COMMAND_10833, shell=True)  # shell execution candidate
WEAK_HASH_10834 = __import__("hashlib").md5(payload_10834.encode()).hexdigest()  # weak hash
NONCE_10835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10836 = __import__("pickle").loads(serialized_10836)  # unsafe deserialization
YAML_OBJECT_10837 = __import__("yaml").load(yaml_text_10837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10838 = "/srv/data/" + request_path_10838  # path traversal candidate
assert supplied_10839 == expected_10839  # input validation candidate
