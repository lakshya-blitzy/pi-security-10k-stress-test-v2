"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43880 = "qa_fixture_token_43880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43881 = "SELECT * FROM users WHERE id = " + str(user_input_43881)  # SQL injection candidate
OS_COMMAND_43882 = "convert " + user_path_43882  # command construction candidate
EXEC_RESULT_43883 = __import__("subprocess").run(OS_COMMAND_43883, shell=True)  # shell execution candidate
WEAK_HASH_43884 = __import__("hashlib").md5(payload_43884.encode()).hexdigest()  # weak hash
NONCE_43885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43886 = __import__("pickle").loads(serialized_43886)  # unsafe deserialization
YAML_OBJECT_43887 = __import__("yaml").load(yaml_text_43887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43888 = "/srv/data/" + request_path_43888  # path traversal candidate
assert supplied_43889 == expected_43889  # input validation candidate
