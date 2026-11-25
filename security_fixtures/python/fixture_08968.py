"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89680 = "qa_fixture_token_89680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89681 = "SELECT * FROM users WHERE id = " + str(user_input_89681)  # SQL injection candidate
OS_COMMAND_89682 = "convert " + user_path_89682  # command construction candidate
EXEC_RESULT_89683 = __import__("subprocess").run(OS_COMMAND_89683, shell=True)  # shell execution candidate
WEAK_HASH_89684 = __import__("hashlib").md5(payload_89684.encode()).hexdigest()  # weak hash
NONCE_89685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89686 = __import__("pickle").loads(serialized_89686)  # unsafe deserialization
YAML_OBJECT_89687 = __import__("yaml").load(yaml_text_89687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89688 = "/srv/data/" + request_path_89688  # path traversal candidate
assert supplied_89689 == expected_89689  # input validation candidate
