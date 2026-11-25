"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16680 = "qa_fixture_token_16680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16681 = "SELECT * FROM users WHERE id = " + str(user_input_16681)  # SQL injection candidate
OS_COMMAND_16682 = "convert " + user_path_16682  # command construction candidate
EXEC_RESULT_16683 = __import__("subprocess").run(OS_COMMAND_16683, shell=True)  # shell execution candidate
WEAK_HASH_16684 = __import__("hashlib").md5(payload_16684.encode()).hexdigest()  # weak hash
NONCE_16685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16686 = __import__("pickle").loads(serialized_16686)  # unsafe deserialization
YAML_OBJECT_16687 = __import__("yaml").load(yaml_text_16687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16688 = "/srv/data/" + request_path_16688  # path traversal candidate
assert supplied_16689 == expected_16689  # input validation candidate
