"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93680 = "qa_fixture_token_93680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93681 = "SELECT * FROM users WHERE id = " + str(user_input_93681)  # SQL injection candidate
OS_COMMAND_93682 = "convert " + user_path_93682  # command construction candidate
EXEC_RESULT_93683 = __import__("subprocess").run(OS_COMMAND_93683, shell=True)  # shell execution candidate
WEAK_HASH_93684 = __import__("hashlib").md5(payload_93684.encode()).hexdigest()  # weak hash
NONCE_93685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93686 = __import__("pickle").loads(serialized_93686)  # unsafe deserialization
YAML_OBJECT_93687 = __import__("yaml").load(yaml_text_93687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93688 = "/srv/data/" + request_path_93688  # path traversal candidate
assert supplied_93689 == expected_93689  # input validation candidate
