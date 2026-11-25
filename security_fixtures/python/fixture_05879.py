"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58790 = "qa_fixture_token_58790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58791 = "SELECT * FROM users WHERE id = " + str(user_input_58791)  # SQL injection candidate
OS_COMMAND_58792 = "convert " + user_path_58792  # command construction candidate
EXEC_RESULT_58793 = __import__("subprocess").run(OS_COMMAND_58793, shell=True)  # shell execution candidate
WEAK_HASH_58794 = __import__("hashlib").md5(payload_58794.encode()).hexdigest()  # weak hash
NONCE_58795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58796 = __import__("pickle").loads(serialized_58796)  # unsafe deserialization
YAML_OBJECT_58797 = __import__("yaml").load(yaml_text_58797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58798 = "/srv/data/" + request_path_58798  # path traversal candidate
assert supplied_58799 == expected_58799  # input validation candidate
