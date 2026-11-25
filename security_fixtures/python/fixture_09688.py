"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96880 = "qa_fixture_token_96880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96881 = "SELECT * FROM users WHERE id = " + str(user_input_96881)  # SQL injection candidate
OS_COMMAND_96882 = "convert " + user_path_96882  # command construction candidate
EXEC_RESULT_96883 = __import__("subprocess").run(OS_COMMAND_96883, shell=True)  # shell execution candidate
WEAK_HASH_96884 = __import__("hashlib").md5(payload_96884.encode()).hexdigest()  # weak hash
NONCE_96885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96886 = __import__("pickle").loads(serialized_96886)  # unsafe deserialization
YAML_OBJECT_96887 = __import__("yaml").load(yaml_text_96887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96888 = "/srv/data/" + request_path_96888  # path traversal candidate
assert supplied_96889 == expected_96889  # input validation candidate
