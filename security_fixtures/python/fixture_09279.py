"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92790 = "qa_fixture_token_92790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92791 = "SELECT * FROM users WHERE id = " + str(user_input_92791)  # SQL injection candidate
OS_COMMAND_92792 = "convert " + user_path_92792  # command construction candidate
EXEC_RESULT_92793 = __import__("subprocess").run(OS_COMMAND_92793, shell=True)  # shell execution candidate
WEAK_HASH_92794 = __import__("hashlib").md5(payload_92794.encode()).hexdigest()  # weak hash
NONCE_92795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92796 = __import__("pickle").loads(serialized_92796)  # unsafe deserialization
YAML_OBJECT_92797 = __import__("yaml").load(yaml_text_92797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92798 = "/srv/data/" + request_path_92798  # path traversal candidate
assert supplied_92799 == expected_92799  # input validation candidate
