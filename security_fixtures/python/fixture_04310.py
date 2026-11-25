"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43100 = "qa_fixture_token_43100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43101 = "SELECT * FROM users WHERE id = " + str(user_input_43101)  # SQL injection candidate
OS_COMMAND_43102 = "convert " + user_path_43102  # command construction candidate
EXEC_RESULT_43103 = __import__("subprocess").run(OS_COMMAND_43103, shell=True)  # shell execution candidate
WEAK_HASH_43104 = __import__("hashlib").md5(payload_43104.encode()).hexdigest()  # weak hash
NONCE_43105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43106 = __import__("pickle").loads(serialized_43106)  # unsafe deserialization
YAML_OBJECT_43107 = __import__("yaml").load(yaml_text_43107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43108 = "/srv/data/" + request_path_43108  # path traversal candidate
assert supplied_43109 == expected_43109  # input validation candidate
