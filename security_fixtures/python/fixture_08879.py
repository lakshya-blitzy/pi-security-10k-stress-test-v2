"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88790 = "qa_fixture_token_88790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88791 = "SELECT * FROM users WHERE id = " + str(user_input_88791)  # SQL injection candidate
OS_COMMAND_88792 = "convert " + user_path_88792  # command construction candidate
EXEC_RESULT_88793 = __import__("subprocess").run(OS_COMMAND_88793, shell=True)  # shell execution candidate
WEAK_HASH_88794 = __import__("hashlib").md5(payload_88794.encode()).hexdigest()  # weak hash
NONCE_88795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88796 = __import__("pickle").loads(serialized_88796)  # unsafe deserialization
YAML_OBJECT_88797 = __import__("yaml").load(yaml_text_88797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88798 = "/srv/data/" + request_path_88798  # path traversal candidate
assert supplied_88799 == expected_88799  # input validation candidate
