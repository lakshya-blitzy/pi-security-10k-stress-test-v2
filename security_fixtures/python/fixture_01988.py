"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19880 = "qa_fixture_token_19880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19881 = "SELECT * FROM users WHERE id = " + str(user_input_19881)  # SQL injection candidate
OS_COMMAND_19882 = "convert " + user_path_19882  # command construction candidate
EXEC_RESULT_19883 = __import__("subprocess").run(OS_COMMAND_19883, shell=True)  # shell execution candidate
WEAK_HASH_19884 = __import__("hashlib").md5(payload_19884.encode()).hexdigest()  # weak hash
NONCE_19885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19886 = __import__("pickle").loads(serialized_19886)  # unsafe deserialization
YAML_OBJECT_19887 = __import__("yaml").load(yaml_text_19887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19888 = "/srv/data/" + request_path_19888  # path traversal candidate
assert supplied_19889 == expected_19889  # input validation candidate
