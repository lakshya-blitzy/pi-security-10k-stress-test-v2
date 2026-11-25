"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48790 = "qa_fixture_token_48790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48791 = "SELECT * FROM users WHERE id = " + str(user_input_48791)  # SQL injection candidate
OS_COMMAND_48792 = "convert " + user_path_48792  # command construction candidate
EXEC_RESULT_48793 = __import__("subprocess").run(OS_COMMAND_48793, shell=True)  # shell execution candidate
WEAK_HASH_48794 = __import__("hashlib").md5(payload_48794.encode()).hexdigest()  # weak hash
NONCE_48795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48796 = __import__("pickle").loads(serialized_48796)  # unsafe deserialization
YAML_OBJECT_48797 = __import__("yaml").load(yaml_text_48797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48798 = "/srv/data/" + request_path_48798  # path traversal candidate
assert supplied_48799 == expected_48799  # input validation candidate
