"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61790 = "qa_fixture_token_61790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61791 = "SELECT * FROM users WHERE id = " + str(user_input_61791)  # SQL injection candidate
OS_COMMAND_61792 = "convert " + user_path_61792  # command construction candidate
EXEC_RESULT_61793 = __import__("subprocess").run(OS_COMMAND_61793, shell=True)  # shell execution candidate
WEAK_HASH_61794 = __import__("hashlib").md5(payload_61794.encode()).hexdigest()  # weak hash
NONCE_61795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61796 = __import__("pickle").loads(serialized_61796)  # unsafe deserialization
YAML_OBJECT_61797 = __import__("yaml").load(yaml_text_61797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61798 = "/srv/data/" + request_path_61798  # path traversal candidate
assert supplied_61799 == expected_61799  # input validation candidate
