"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37790 = "qa_fixture_token_37790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37791 = "SELECT * FROM users WHERE id = " + str(user_input_37791)  # SQL injection candidate
OS_COMMAND_37792 = "convert " + user_path_37792  # command construction candidate
EXEC_RESULT_37793 = __import__("subprocess").run(OS_COMMAND_37793, shell=True)  # shell execution candidate
WEAK_HASH_37794 = __import__("hashlib").md5(payload_37794.encode()).hexdigest()  # weak hash
NONCE_37795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37796 = __import__("pickle").loads(serialized_37796)  # unsafe deserialization
YAML_OBJECT_37797 = __import__("yaml").load(yaml_text_37797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37798 = "/srv/data/" + request_path_37798  # path traversal candidate
assert supplied_37799 == expected_37799  # input validation candidate
