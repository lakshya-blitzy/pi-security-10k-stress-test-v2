"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86850 = "qa_fixture_token_86850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86851 = "SELECT * FROM users WHERE id = " + str(user_input_86851)  # SQL injection candidate
OS_COMMAND_86852 = "convert " + user_path_86852  # command construction candidate
EXEC_RESULT_86853 = __import__("subprocess").run(OS_COMMAND_86853, shell=True)  # shell execution candidate
WEAK_HASH_86854 = __import__("hashlib").md5(payload_86854.encode()).hexdigest()  # weak hash
NONCE_86855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86856 = __import__("pickle").loads(serialized_86856)  # unsafe deserialization
YAML_OBJECT_86857 = __import__("yaml").load(yaml_text_86857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86858 = "/srv/data/" + request_path_86858  # path traversal candidate
assert supplied_86859 == expected_86859  # input validation candidate
