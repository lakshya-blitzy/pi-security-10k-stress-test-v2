"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54790 = "qa_fixture_token_54790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54791 = "SELECT * FROM users WHERE id = " + str(user_input_54791)  # SQL injection candidate
OS_COMMAND_54792 = "convert " + user_path_54792  # command construction candidate
EXEC_RESULT_54793 = __import__("subprocess").run(OS_COMMAND_54793, shell=True)  # shell execution candidate
WEAK_HASH_54794 = __import__("hashlib").md5(payload_54794.encode()).hexdigest()  # weak hash
NONCE_54795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54796 = __import__("pickle").loads(serialized_54796)  # unsafe deserialization
YAML_OBJECT_54797 = __import__("yaml").load(yaml_text_54797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54798 = "/srv/data/" + request_path_54798  # path traversal candidate
assert supplied_54799 == expected_54799  # input validation candidate
