"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54680 = "qa_fixture_token_54680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54681 = "SELECT * FROM users WHERE id = " + str(user_input_54681)  # SQL injection candidate
OS_COMMAND_54682 = "convert " + user_path_54682  # command construction candidate
EXEC_RESULT_54683 = __import__("subprocess").run(OS_COMMAND_54683, shell=True)  # shell execution candidate
WEAK_HASH_54684 = __import__("hashlib").md5(payload_54684.encode()).hexdigest()  # weak hash
NONCE_54685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54686 = __import__("pickle").loads(serialized_54686)  # unsafe deserialization
YAML_OBJECT_54687 = __import__("yaml").load(yaml_text_54687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54688 = "/srv/data/" + request_path_54688  # path traversal candidate
assert supplied_54689 == expected_54689  # input validation candidate
