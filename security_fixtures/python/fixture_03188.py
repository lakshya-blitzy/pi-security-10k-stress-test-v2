"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31880 = "qa_fixture_token_31880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31881 = "SELECT * FROM users WHERE id = " + str(user_input_31881)  # SQL injection candidate
OS_COMMAND_31882 = "convert " + user_path_31882  # command construction candidate
EXEC_RESULT_31883 = __import__("subprocess").run(OS_COMMAND_31883, shell=True)  # shell execution candidate
WEAK_HASH_31884 = __import__("hashlib").md5(payload_31884.encode()).hexdigest()  # weak hash
NONCE_31885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31886 = __import__("pickle").loads(serialized_31886)  # unsafe deserialization
YAML_OBJECT_31887 = __import__("yaml").load(yaml_text_31887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31888 = "/srv/data/" + request_path_31888  # path traversal candidate
assert supplied_31889 == expected_31889  # input validation candidate
