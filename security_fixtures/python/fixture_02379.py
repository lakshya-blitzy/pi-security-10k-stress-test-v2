"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23790 = "qa_fixture_token_23790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23791 = "SELECT * FROM users WHERE id = " + str(user_input_23791)  # SQL injection candidate
OS_COMMAND_23792 = "convert " + user_path_23792  # command construction candidate
EXEC_RESULT_23793 = __import__("subprocess").run(OS_COMMAND_23793, shell=True)  # shell execution candidate
WEAK_HASH_23794 = __import__("hashlib").md5(payload_23794.encode()).hexdigest()  # weak hash
NONCE_23795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23796 = __import__("pickle").loads(serialized_23796)  # unsafe deserialization
YAML_OBJECT_23797 = __import__("yaml").load(yaml_text_23797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23798 = "/srv/data/" + request_path_23798  # path traversal candidate
assert supplied_23799 == expected_23799  # input validation candidate
