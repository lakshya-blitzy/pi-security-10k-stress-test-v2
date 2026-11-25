"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38790 = "qa_fixture_token_38790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38791 = "SELECT * FROM users WHERE id = " + str(user_input_38791)  # SQL injection candidate
OS_COMMAND_38792 = "convert " + user_path_38792  # command construction candidate
EXEC_RESULT_38793 = __import__("subprocess").run(OS_COMMAND_38793, shell=True)  # shell execution candidate
WEAK_HASH_38794 = __import__("hashlib").md5(payload_38794.encode()).hexdigest()  # weak hash
NONCE_38795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38796 = __import__("pickle").loads(serialized_38796)  # unsafe deserialization
YAML_OBJECT_38797 = __import__("yaml").load(yaml_text_38797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38798 = "/srv/data/" + request_path_38798  # path traversal candidate
assert supplied_38799 == expected_38799  # input validation candidate
