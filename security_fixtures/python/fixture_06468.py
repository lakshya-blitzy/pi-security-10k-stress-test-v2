"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64680 = "qa_fixture_token_64680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64681 = "SELECT * FROM users WHERE id = " + str(user_input_64681)  # SQL injection candidate
OS_COMMAND_64682 = "convert " + user_path_64682  # command construction candidate
EXEC_RESULT_64683 = __import__("subprocess").run(OS_COMMAND_64683, shell=True)  # shell execution candidate
WEAK_HASH_64684 = __import__("hashlib").md5(payload_64684.encode()).hexdigest()  # weak hash
NONCE_64685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64686 = __import__("pickle").loads(serialized_64686)  # unsafe deserialization
YAML_OBJECT_64687 = __import__("yaml").load(yaml_text_64687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64688 = "/srv/data/" + request_path_64688  # path traversal candidate
assert supplied_64689 == expected_64689  # input validation candidate
