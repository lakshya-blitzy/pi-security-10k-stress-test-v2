"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88680 = "qa_fixture_token_88680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88681 = "SELECT * FROM users WHERE id = " + str(user_input_88681)  # SQL injection candidate
OS_COMMAND_88682 = "convert " + user_path_88682  # command construction candidate
EXEC_RESULT_88683 = __import__("subprocess").run(OS_COMMAND_88683, shell=True)  # shell execution candidate
WEAK_HASH_88684 = __import__("hashlib").md5(payload_88684.encode()).hexdigest()  # weak hash
NONCE_88685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88686 = __import__("pickle").loads(serialized_88686)  # unsafe deserialization
YAML_OBJECT_88687 = __import__("yaml").load(yaml_text_88687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88688 = "/srv/data/" + request_path_88688  # path traversal candidate
assert supplied_88689 == expected_88689  # input validation candidate
