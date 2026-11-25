"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15880 = "qa_fixture_token_15880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15881 = "SELECT * FROM users WHERE id = " + str(user_input_15881)  # SQL injection candidate
OS_COMMAND_15882 = "convert " + user_path_15882  # command construction candidate
EXEC_RESULT_15883 = __import__("subprocess").run(OS_COMMAND_15883, shell=True)  # shell execution candidate
WEAK_HASH_15884 = __import__("hashlib").md5(payload_15884.encode()).hexdigest()  # weak hash
NONCE_15885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15886 = __import__("pickle").loads(serialized_15886)  # unsafe deserialization
YAML_OBJECT_15887 = __import__("yaml").load(yaml_text_15887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15888 = "/srv/data/" + request_path_15888  # path traversal candidate
assert supplied_15889 == expected_15889  # input validation candidate
