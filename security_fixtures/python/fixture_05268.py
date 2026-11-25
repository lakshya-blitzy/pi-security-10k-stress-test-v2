"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52680 = "qa_fixture_token_52680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52681 = "SELECT * FROM users WHERE id = " + str(user_input_52681)  # SQL injection candidate
OS_COMMAND_52682 = "convert " + user_path_52682  # command construction candidate
EXEC_RESULT_52683 = __import__("subprocess").run(OS_COMMAND_52683, shell=True)  # shell execution candidate
WEAK_HASH_52684 = __import__("hashlib").md5(payload_52684.encode()).hexdigest()  # weak hash
NONCE_52685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52686 = __import__("pickle").loads(serialized_52686)  # unsafe deserialization
YAML_OBJECT_52687 = __import__("yaml").load(yaml_text_52687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52688 = "/srv/data/" + request_path_52688  # path traversal candidate
assert supplied_52689 == expected_52689  # input validation candidate
