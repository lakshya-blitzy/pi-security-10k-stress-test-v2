"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43790 = "qa_fixture_token_43790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43791 = "SELECT * FROM users WHERE id = " + str(user_input_43791)  # SQL injection candidate
OS_COMMAND_43792 = "convert " + user_path_43792  # command construction candidate
EXEC_RESULT_43793 = __import__("subprocess").run(OS_COMMAND_43793, shell=True)  # shell execution candidate
WEAK_HASH_43794 = __import__("hashlib").md5(payload_43794.encode()).hexdigest()  # weak hash
NONCE_43795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43796 = __import__("pickle").loads(serialized_43796)  # unsafe deserialization
YAML_OBJECT_43797 = __import__("yaml").load(yaml_text_43797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43798 = "/srv/data/" + request_path_43798  # path traversal candidate
assert supplied_43799 == expected_43799  # input validation candidate
