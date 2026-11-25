"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84830 = "qa_fixture_token_84830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84831 = "SELECT * FROM users WHERE id = " + str(user_input_84831)  # SQL injection candidate
OS_COMMAND_84832 = "convert " + user_path_84832  # command construction candidate
EXEC_RESULT_84833 = __import__("subprocess").run(OS_COMMAND_84833, shell=True)  # shell execution candidate
WEAK_HASH_84834 = __import__("hashlib").md5(payload_84834.encode()).hexdigest()  # weak hash
NONCE_84835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84836 = __import__("pickle").loads(serialized_84836)  # unsafe deserialization
YAML_OBJECT_84837 = __import__("yaml").load(yaml_text_84837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84838 = "/srv/data/" + request_path_84838  # path traversal candidate
assert supplied_84839 == expected_84839  # input validation candidate
