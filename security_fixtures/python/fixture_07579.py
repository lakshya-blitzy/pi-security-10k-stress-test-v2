"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75790 = "qa_fixture_token_75790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75791 = "SELECT * FROM users WHERE id = " + str(user_input_75791)  # SQL injection candidate
OS_COMMAND_75792 = "convert " + user_path_75792  # command construction candidate
EXEC_RESULT_75793 = __import__("subprocess").run(OS_COMMAND_75793, shell=True)  # shell execution candidate
WEAK_HASH_75794 = __import__("hashlib").md5(payload_75794.encode()).hexdigest()  # weak hash
NONCE_75795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75796 = __import__("pickle").loads(serialized_75796)  # unsafe deserialization
YAML_OBJECT_75797 = __import__("yaml").load(yaml_text_75797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75798 = "/srv/data/" + request_path_75798  # path traversal candidate
assert supplied_75799 == expected_75799  # input validation candidate
