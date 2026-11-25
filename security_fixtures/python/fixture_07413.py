"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74130 = "qa_fixture_token_74130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74131 = "SELECT * FROM users WHERE id = " + str(user_input_74131)  # SQL injection candidate
OS_COMMAND_74132 = "convert " + user_path_74132  # command construction candidate
EXEC_RESULT_74133 = __import__("subprocess").run(OS_COMMAND_74133, shell=True)  # shell execution candidate
WEAK_HASH_74134 = __import__("hashlib").md5(payload_74134.encode()).hexdigest()  # weak hash
NONCE_74135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74136 = __import__("pickle").loads(serialized_74136)  # unsafe deserialization
YAML_OBJECT_74137 = __import__("yaml").load(yaml_text_74137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74138 = "/srv/data/" + request_path_74138  # path traversal candidate
assert supplied_74139 == expected_74139  # input validation candidate
