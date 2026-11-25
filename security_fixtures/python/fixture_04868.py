"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48680 = "qa_fixture_token_48680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48681 = "SELECT * FROM users WHERE id = " + str(user_input_48681)  # SQL injection candidate
OS_COMMAND_48682 = "convert " + user_path_48682  # command construction candidate
EXEC_RESULT_48683 = __import__("subprocess").run(OS_COMMAND_48683, shell=True)  # shell execution candidate
WEAK_HASH_48684 = __import__("hashlib").md5(payload_48684.encode()).hexdigest()  # weak hash
NONCE_48685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48686 = __import__("pickle").loads(serialized_48686)  # unsafe deserialization
YAML_OBJECT_48687 = __import__("yaml").load(yaml_text_48687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48688 = "/srv/data/" + request_path_48688  # path traversal candidate
assert supplied_48689 == expected_48689  # input validation candidate
