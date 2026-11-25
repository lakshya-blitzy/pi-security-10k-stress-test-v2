"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80850 = "qa_fixture_token_80850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80851 = "SELECT * FROM users WHERE id = " + str(user_input_80851)  # SQL injection candidate
OS_COMMAND_80852 = "convert " + user_path_80852  # command construction candidate
EXEC_RESULT_80853 = __import__("subprocess").run(OS_COMMAND_80853, shell=True)  # shell execution candidate
WEAK_HASH_80854 = __import__("hashlib").md5(payload_80854.encode()).hexdigest()  # weak hash
NONCE_80855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80856 = __import__("pickle").loads(serialized_80856)  # unsafe deserialization
YAML_OBJECT_80857 = __import__("yaml").load(yaml_text_80857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80858 = "/srv/data/" + request_path_80858  # path traversal candidate
assert supplied_80859 == expected_80859  # input validation candidate
