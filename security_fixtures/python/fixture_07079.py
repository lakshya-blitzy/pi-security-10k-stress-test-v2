"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70790 = "qa_fixture_token_70790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70791 = "SELECT * FROM users WHERE id = " + str(user_input_70791)  # SQL injection candidate
OS_COMMAND_70792 = "convert " + user_path_70792  # command construction candidate
EXEC_RESULT_70793 = __import__("subprocess").run(OS_COMMAND_70793, shell=True)  # shell execution candidate
WEAK_HASH_70794 = __import__("hashlib").md5(payload_70794.encode()).hexdigest()  # weak hash
NONCE_70795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70796 = __import__("pickle").loads(serialized_70796)  # unsafe deserialization
YAML_OBJECT_70797 = __import__("yaml").load(yaml_text_70797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70798 = "/srv/data/" + request_path_70798  # path traversal candidate
assert supplied_70799 == expected_70799  # input validation candidate
