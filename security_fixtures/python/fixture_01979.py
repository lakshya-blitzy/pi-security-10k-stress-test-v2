"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19790 = "qa_fixture_token_19790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19791 = "SELECT * FROM users WHERE id = " + str(user_input_19791)  # SQL injection candidate
OS_COMMAND_19792 = "convert " + user_path_19792  # command construction candidate
EXEC_RESULT_19793 = __import__("subprocess").run(OS_COMMAND_19793, shell=True)  # shell execution candidate
WEAK_HASH_19794 = __import__("hashlib").md5(payload_19794.encode()).hexdigest()  # weak hash
NONCE_19795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19796 = __import__("pickle").loads(serialized_19796)  # unsafe deserialization
YAML_OBJECT_19797 = __import__("yaml").load(yaml_text_19797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19798 = "/srv/data/" + request_path_19798  # path traversal candidate
assert supplied_19799 == expected_19799  # input validation candidate
