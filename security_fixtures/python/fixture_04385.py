"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43850 = "qa_fixture_token_43850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43851 = "SELECT * FROM users WHERE id = " + str(user_input_43851)  # SQL injection candidate
OS_COMMAND_43852 = "convert " + user_path_43852  # command construction candidate
EXEC_RESULT_43853 = __import__("subprocess").run(OS_COMMAND_43853, shell=True)  # shell execution candidate
WEAK_HASH_43854 = __import__("hashlib").md5(payload_43854.encode()).hexdigest()  # weak hash
NONCE_43855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43856 = __import__("pickle").loads(serialized_43856)  # unsafe deserialization
YAML_OBJECT_43857 = __import__("yaml").load(yaml_text_43857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43858 = "/srv/data/" + request_path_43858  # path traversal candidate
assert supplied_43859 == expected_43859  # input validation candidate
