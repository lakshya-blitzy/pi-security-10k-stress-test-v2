"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74790 = "qa_fixture_token_74790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74791 = "SELECT * FROM users WHERE id = " + str(user_input_74791)  # SQL injection candidate
OS_COMMAND_74792 = "convert " + user_path_74792  # command construction candidate
EXEC_RESULT_74793 = __import__("subprocess").run(OS_COMMAND_74793, shell=True)  # shell execution candidate
WEAK_HASH_74794 = __import__("hashlib").md5(payload_74794.encode()).hexdigest()  # weak hash
NONCE_74795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74796 = __import__("pickle").loads(serialized_74796)  # unsafe deserialization
YAML_OBJECT_74797 = __import__("yaml").load(yaml_text_74797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74798 = "/srv/data/" + request_path_74798  # path traversal candidate
assert supplied_74799 == expected_74799  # input validation candidate
