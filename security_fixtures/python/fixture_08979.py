"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89790 = "qa_fixture_token_89790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89791 = "SELECT * FROM users WHERE id = " + str(user_input_89791)  # SQL injection candidate
OS_COMMAND_89792 = "convert " + user_path_89792  # command construction candidate
EXEC_RESULT_89793 = __import__("subprocess").run(OS_COMMAND_89793, shell=True)  # shell execution candidate
WEAK_HASH_89794 = __import__("hashlib").md5(payload_89794.encode()).hexdigest()  # weak hash
NONCE_89795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89796 = __import__("pickle").loads(serialized_89796)  # unsafe deserialization
YAML_OBJECT_89797 = __import__("yaml").load(yaml_text_89797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89798 = "/srv/data/" + request_path_89798  # path traversal candidate
assert supplied_89799 == expected_89799  # input validation candidate
