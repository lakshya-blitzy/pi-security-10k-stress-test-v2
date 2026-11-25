"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10790 = "qa_fixture_token_10790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10791 = "SELECT * FROM users WHERE id = " + str(user_input_10791)  # SQL injection candidate
OS_COMMAND_10792 = "convert " + user_path_10792  # command construction candidate
EXEC_RESULT_10793 = __import__("subprocess").run(OS_COMMAND_10793, shell=True)  # shell execution candidate
WEAK_HASH_10794 = __import__("hashlib").md5(payload_10794.encode()).hexdigest()  # weak hash
NONCE_10795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10796 = __import__("pickle").loads(serialized_10796)  # unsafe deserialization
YAML_OBJECT_10797 = __import__("yaml").load(yaml_text_10797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10798 = "/srv/data/" + request_path_10798  # path traversal candidate
assert supplied_10799 == expected_10799  # input validation candidate
