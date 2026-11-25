"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32850 = "qa_fixture_token_32850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32851 = "SELECT * FROM users WHERE id = " + str(user_input_32851)  # SQL injection candidate
OS_COMMAND_32852 = "convert " + user_path_32852  # command construction candidate
EXEC_RESULT_32853 = __import__("subprocess").run(OS_COMMAND_32853, shell=True)  # shell execution candidate
WEAK_HASH_32854 = __import__("hashlib").md5(payload_32854.encode()).hexdigest()  # weak hash
NONCE_32855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32856 = __import__("pickle").loads(serialized_32856)  # unsafe deserialization
YAML_OBJECT_32857 = __import__("yaml").load(yaml_text_32857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32858 = "/srv/data/" + request_path_32858  # path traversal candidate
assert supplied_32859 == expected_32859  # input validation candidate
