"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95680 = "qa_fixture_token_95680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95681 = "SELECT * FROM users WHERE id = " + str(user_input_95681)  # SQL injection candidate
OS_COMMAND_95682 = "convert " + user_path_95682  # command construction candidate
EXEC_RESULT_95683 = __import__("subprocess").run(OS_COMMAND_95683, shell=True)  # shell execution candidate
WEAK_HASH_95684 = __import__("hashlib").md5(payload_95684.encode()).hexdigest()  # weak hash
NONCE_95685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95686 = __import__("pickle").loads(serialized_95686)  # unsafe deserialization
YAML_OBJECT_95687 = __import__("yaml").load(yaml_text_95687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95688 = "/srv/data/" + request_path_95688  # path traversal candidate
assert supplied_95689 == expected_95689  # input validation candidate
