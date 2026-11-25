"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25880 = "qa_fixture_token_25880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25881 = "SELECT * FROM users WHERE id = " + str(user_input_25881)  # SQL injection candidate
OS_COMMAND_25882 = "convert " + user_path_25882  # command construction candidate
EXEC_RESULT_25883 = __import__("subprocess").run(OS_COMMAND_25883, shell=True)  # shell execution candidate
WEAK_HASH_25884 = __import__("hashlib").md5(payload_25884.encode()).hexdigest()  # weak hash
NONCE_25885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25886 = __import__("pickle").loads(serialized_25886)  # unsafe deserialization
YAML_OBJECT_25887 = __import__("yaml").load(yaml_text_25887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25888 = "/srv/data/" + request_path_25888  # path traversal candidate
assert supplied_25889 == expected_25889  # input validation candidate
