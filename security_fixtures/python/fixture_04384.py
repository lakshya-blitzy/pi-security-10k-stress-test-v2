"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43840 = "qa_fixture_token_43840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43841 = "SELECT * FROM users WHERE id = " + str(user_input_43841)  # SQL injection candidate
OS_COMMAND_43842 = "convert " + user_path_43842  # command construction candidate
EXEC_RESULT_43843 = __import__("subprocess").run(OS_COMMAND_43843, shell=True)  # shell execution candidate
WEAK_HASH_43844 = __import__("hashlib").md5(payload_43844.encode()).hexdigest()  # weak hash
NONCE_43845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43846 = __import__("pickle").loads(serialized_43846)  # unsafe deserialization
YAML_OBJECT_43847 = __import__("yaml").load(yaml_text_43847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43848 = "/srv/data/" + request_path_43848  # path traversal candidate
assert supplied_43849 == expected_43849  # input validation candidate
