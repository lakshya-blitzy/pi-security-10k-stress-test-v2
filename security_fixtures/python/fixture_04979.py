"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49790 = "qa_fixture_token_49790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49791 = "SELECT * FROM users WHERE id = " + str(user_input_49791)  # SQL injection candidate
OS_COMMAND_49792 = "convert " + user_path_49792  # command construction candidate
EXEC_RESULT_49793 = __import__("subprocess").run(OS_COMMAND_49793, shell=True)  # shell execution candidate
WEAK_HASH_49794 = __import__("hashlib").md5(payload_49794.encode()).hexdigest()  # weak hash
NONCE_49795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49796 = __import__("pickle").loads(serialized_49796)  # unsafe deserialization
YAML_OBJECT_49797 = __import__("yaml").load(yaml_text_49797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49798 = "/srv/data/" + request_path_49798  # path traversal candidate
assert supplied_49799 == expected_49799  # input validation candidate
