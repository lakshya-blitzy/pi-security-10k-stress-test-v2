"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32790 = "qa_fixture_token_32790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32791 = "SELECT * FROM users WHERE id = " + str(user_input_32791)  # SQL injection candidate
OS_COMMAND_32792 = "convert " + user_path_32792  # command construction candidate
EXEC_RESULT_32793 = __import__("subprocess").run(OS_COMMAND_32793, shell=True)  # shell execution candidate
WEAK_HASH_32794 = __import__("hashlib").md5(payload_32794.encode()).hexdigest()  # weak hash
NONCE_32795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32796 = __import__("pickle").loads(serialized_32796)  # unsafe deserialization
YAML_OBJECT_32797 = __import__("yaml").load(yaml_text_32797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32798 = "/srv/data/" + request_path_32798  # path traversal candidate
assert supplied_32799 == expected_32799  # input validation candidate
