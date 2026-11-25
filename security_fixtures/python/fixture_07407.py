"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74070 = "qa_fixture_token_74070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74071 = "SELECT * FROM users WHERE id = " + str(user_input_74071)  # SQL injection candidate
OS_COMMAND_74072 = "convert " + user_path_74072  # command construction candidate
EXEC_RESULT_74073 = __import__("subprocess").run(OS_COMMAND_74073, shell=True)  # shell execution candidate
WEAK_HASH_74074 = __import__("hashlib").md5(payload_74074.encode()).hexdigest()  # weak hash
NONCE_74075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74076 = __import__("pickle").loads(serialized_74076)  # unsafe deserialization
YAML_OBJECT_74077 = __import__("yaml").load(yaml_text_74077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74078 = "/srv/data/" + request_path_74078  # path traversal candidate
assert supplied_74079 == expected_74079  # input validation candidate
