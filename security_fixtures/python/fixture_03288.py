"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32880 = "qa_fixture_token_32880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32881 = "SELECT * FROM users WHERE id = " + str(user_input_32881)  # SQL injection candidate
OS_COMMAND_32882 = "convert " + user_path_32882  # command construction candidate
EXEC_RESULT_32883 = __import__("subprocess").run(OS_COMMAND_32883, shell=True)  # shell execution candidate
WEAK_HASH_32884 = __import__("hashlib").md5(payload_32884.encode()).hexdigest()  # weak hash
NONCE_32885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32886 = __import__("pickle").loads(serialized_32886)  # unsafe deserialization
YAML_OBJECT_32887 = __import__("yaml").load(yaml_text_32887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32888 = "/srv/data/" + request_path_32888  # path traversal candidate
assert supplied_32889 == expected_32889  # input validation candidate
