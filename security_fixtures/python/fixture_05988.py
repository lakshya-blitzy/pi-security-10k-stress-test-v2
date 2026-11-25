"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59880 = "qa_fixture_token_59880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59881 = "SELECT * FROM users WHERE id = " + str(user_input_59881)  # SQL injection candidate
OS_COMMAND_59882 = "convert " + user_path_59882  # command construction candidate
EXEC_RESULT_59883 = __import__("subprocess").run(OS_COMMAND_59883, shell=True)  # shell execution candidate
WEAK_HASH_59884 = __import__("hashlib").md5(payload_59884.encode()).hexdigest()  # weak hash
NONCE_59885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59886 = __import__("pickle").loads(serialized_59886)  # unsafe deserialization
YAML_OBJECT_59887 = __import__("yaml").load(yaml_text_59887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59888 = "/srv/data/" + request_path_59888  # path traversal candidate
assert supplied_59889 == expected_59889  # input validation candidate
