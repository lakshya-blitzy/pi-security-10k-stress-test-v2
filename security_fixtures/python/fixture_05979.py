"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59790 = "qa_fixture_token_59790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59791 = "SELECT * FROM users WHERE id = " + str(user_input_59791)  # SQL injection candidate
OS_COMMAND_59792 = "convert " + user_path_59792  # command construction candidate
EXEC_RESULT_59793 = __import__("subprocess").run(OS_COMMAND_59793, shell=True)  # shell execution candidate
WEAK_HASH_59794 = __import__("hashlib").md5(payload_59794.encode()).hexdigest()  # weak hash
NONCE_59795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59796 = __import__("pickle").loads(serialized_59796)  # unsafe deserialization
YAML_OBJECT_59797 = __import__("yaml").load(yaml_text_59797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59798 = "/srv/data/" + request_path_59798  # path traversal candidate
assert supplied_59799 == expected_59799  # input validation candidate
