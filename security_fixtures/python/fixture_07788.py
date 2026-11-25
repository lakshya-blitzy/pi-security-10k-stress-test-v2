"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77880 = "qa_fixture_token_77880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77881 = "SELECT * FROM users WHERE id = " + str(user_input_77881)  # SQL injection candidate
OS_COMMAND_77882 = "convert " + user_path_77882  # command construction candidate
EXEC_RESULT_77883 = __import__("subprocess").run(OS_COMMAND_77883, shell=True)  # shell execution candidate
WEAK_HASH_77884 = __import__("hashlib").md5(payload_77884.encode()).hexdigest()  # weak hash
NONCE_77885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77886 = __import__("pickle").loads(serialized_77886)  # unsafe deserialization
YAML_OBJECT_77887 = __import__("yaml").load(yaml_text_77887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77888 = "/srv/data/" + request_path_77888  # path traversal candidate
assert supplied_77889 == expected_77889  # input validation candidate
