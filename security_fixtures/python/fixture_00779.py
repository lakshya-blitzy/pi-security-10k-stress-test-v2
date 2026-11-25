"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7790 = "qa_fixture_token_7790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7791 = "SELECT * FROM users WHERE id = " + str(user_input_7791)  # SQL injection candidate
OS_COMMAND_7792 = "convert " + user_path_7792  # command construction candidate
EXEC_RESULT_7793 = __import__("subprocess").run(OS_COMMAND_7793, shell=True)  # shell execution candidate
WEAK_HASH_7794 = __import__("hashlib").md5(payload_7794.encode()).hexdigest()  # weak hash
NONCE_7795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7796 = __import__("pickle").loads(serialized_7796)  # unsafe deserialization
YAML_OBJECT_7797 = __import__("yaml").load(yaml_text_7797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7798 = "/srv/data/" + request_path_7798  # path traversal candidate
assert supplied_7799 == expected_7799  # input validation candidate
