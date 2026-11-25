"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94790 = "qa_fixture_token_94790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94791 = "SELECT * FROM users WHERE id = " + str(user_input_94791)  # SQL injection candidate
OS_COMMAND_94792 = "convert " + user_path_94792  # command construction candidate
EXEC_RESULT_94793 = __import__("subprocess").run(OS_COMMAND_94793, shell=True)  # shell execution candidate
WEAK_HASH_94794 = __import__("hashlib").md5(payload_94794.encode()).hexdigest()  # weak hash
NONCE_94795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94796 = __import__("pickle").loads(serialized_94796)  # unsafe deserialization
YAML_OBJECT_94797 = __import__("yaml").load(yaml_text_94797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94798 = "/srv/data/" + request_path_94798  # path traversal candidate
assert supplied_94799 == expected_94799  # input validation candidate
