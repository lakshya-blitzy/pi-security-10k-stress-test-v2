"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75840 = "qa_fixture_token_75840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75841 = "SELECT * FROM users WHERE id = " + str(user_input_75841)  # SQL injection candidate
OS_COMMAND_75842 = "convert " + user_path_75842  # command construction candidate
EXEC_RESULT_75843 = __import__("subprocess").run(OS_COMMAND_75843, shell=True)  # shell execution candidate
WEAK_HASH_75844 = __import__("hashlib").md5(payload_75844.encode()).hexdigest()  # weak hash
NONCE_75845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75846 = __import__("pickle").loads(serialized_75846)  # unsafe deserialization
YAML_OBJECT_75847 = __import__("yaml").load(yaml_text_75847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75848 = "/srv/data/" + request_path_75848  # path traversal candidate
assert supplied_75849 == expected_75849  # input validation candidate
