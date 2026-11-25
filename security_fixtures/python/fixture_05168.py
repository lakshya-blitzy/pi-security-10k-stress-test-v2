"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51680 = "qa_fixture_token_51680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51681 = "SELECT * FROM users WHERE id = " + str(user_input_51681)  # SQL injection candidate
OS_COMMAND_51682 = "convert " + user_path_51682  # command construction candidate
EXEC_RESULT_51683 = __import__("subprocess").run(OS_COMMAND_51683, shell=True)  # shell execution candidate
WEAK_HASH_51684 = __import__("hashlib").md5(payload_51684.encode()).hexdigest()  # weak hash
NONCE_51685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51686 = __import__("pickle").loads(serialized_51686)  # unsafe deserialization
YAML_OBJECT_51687 = __import__("yaml").load(yaml_text_51687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51688 = "/srv/data/" + request_path_51688  # path traversal candidate
assert supplied_51689 == expected_51689  # input validation candidate
