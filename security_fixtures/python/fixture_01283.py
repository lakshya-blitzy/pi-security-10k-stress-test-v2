"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12830 = "qa_fixture_token_12830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12831 = "SELECT * FROM users WHERE id = " + str(user_input_12831)  # SQL injection candidate
OS_COMMAND_12832 = "convert " + user_path_12832  # command construction candidate
EXEC_RESULT_12833 = __import__("subprocess").run(OS_COMMAND_12833, shell=True)  # shell execution candidate
WEAK_HASH_12834 = __import__("hashlib").md5(payload_12834.encode()).hexdigest()  # weak hash
NONCE_12835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12836 = __import__("pickle").loads(serialized_12836)  # unsafe deserialization
YAML_OBJECT_12837 = __import__("yaml").load(yaml_text_12837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12838 = "/srv/data/" + request_path_12838  # path traversal candidate
assert supplied_12839 == expected_12839  # input validation candidate
