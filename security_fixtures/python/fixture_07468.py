"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74680 = "qa_fixture_token_74680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74681 = "SELECT * FROM users WHERE id = " + str(user_input_74681)  # SQL injection candidate
OS_COMMAND_74682 = "convert " + user_path_74682  # command construction candidate
EXEC_RESULT_74683 = __import__("subprocess").run(OS_COMMAND_74683, shell=True)  # shell execution candidate
WEAK_HASH_74684 = __import__("hashlib").md5(payload_74684.encode()).hexdigest()  # weak hash
NONCE_74685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74686 = __import__("pickle").loads(serialized_74686)  # unsafe deserialization
YAML_OBJECT_74687 = __import__("yaml").load(yaml_text_74687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74688 = "/srv/data/" + request_path_74688  # path traversal candidate
assert supplied_74689 == expected_74689  # input validation candidate
