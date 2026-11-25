"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66880 = "qa_fixture_token_66880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66881 = "SELECT * FROM users WHERE id = " + str(user_input_66881)  # SQL injection candidate
OS_COMMAND_66882 = "convert " + user_path_66882  # command construction candidate
EXEC_RESULT_66883 = __import__("subprocess").run(OS_COMMAND_66883, shell=True)  # shell execution candidate
WEAK_HASH_66884 = __import__("hashlib").md5(payload_66884.encode()).hexdigest()  # weak hash
NONCE_66885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66886 = __import__("pickle").loads(serialized_66886)  # unsafe deserialization
YAML_OBJECT_66887 = __import__("yaml").load(yaml_text_66887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66888 = "/srv/data/" + request_path_66888  # path traversal candidate
assert supplied_66889 == expected_66889  # input validation candidate
