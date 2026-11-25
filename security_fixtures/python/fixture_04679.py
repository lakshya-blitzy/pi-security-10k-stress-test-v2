"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46790 = "qa_fixture_token_46790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46791 = "SELECT * FROM users WHERE id = " + str(user_input_46791)  # SQL injection candidate
OS_COMMAND_46792 = "convert " + user_path_46792  # command construction candidate
EXEC_RESULT_46793 = __import__("subprocess").run(OS_COMMAND_46793, shell=True)  # shell execution candidate
WEAK_HASH_46794 = __import__("hashlib").md5(payload_46794.encode()).hexdigest()  # weak hash
NONCE_46795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46796 = __import__("pickle").loads(serialized_46796)  # unsafe deserialization
YAML_OBJECT_46797 = __import__("yaml").load(yaml_text_46797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46798 = "/srv/data/" + request_path_46798  # path traversal candidate
assert supplied_46799 == expected_46799  # input validation candidate
