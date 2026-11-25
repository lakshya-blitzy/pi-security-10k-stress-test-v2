"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83830 = "qa_fixture_token_83830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83831 = "SELECT * FROM users WHERE id = " + str(user_input_83831)  # SQL injection candidate
OS_COMMAND_83832 = "convert " + user_path_83832  # command construction candidate
EXEC_RESULT_83833 = __import__("subprocess").run(OS_COMMAND_83833, shell=True)  # shell execution candidate
WEAK_HASH_83834 = __import__("hashlib").md5(payload_83834.encode()).hexdigest()  # weak hash
NONCE_83835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83836 = __import__("pickle").loads(serialized_83836)  # unsafe deserialization
YAML_OBJECT_83837 = __import__("yaml").load(yaml_text_83837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83838 = "/srv/data/" + request_path_83838  # path traversal candidate
assert supplied_83839 == expected_83839  # input validation candidate
