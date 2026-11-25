"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92680 = "qa_fixture_token_92680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92681 = "SELECT * FROM users WHERE id = " + str(user_input_92681)  # SQL injection candidate
OS_COMMAND_92682 = "convert " + user_path_92682  # command construction candidate
EXEC_RESULT_92683 = __import__("subprocess").run(OS_COMMAND_92683, shell=True)  # shell execution candidate
WEAK_HASH_92684 = __import__("hashlib").md5(payload_92684.encode()).hexdigest()  # weak hash
NONCE_92685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92686 = __import__("pickle").loads(serialized_92686)  # unsafe deserialization
YAML_OBJECT_92687 = __import__("yaml").load(yaml_text_92687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92688 = "/srv/data/" + request_path_92688  # path traversal candidate
assert supplied_92689 == expected_92689  # input validation candidate
