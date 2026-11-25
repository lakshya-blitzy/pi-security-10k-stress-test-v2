"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92110 = "qa_fixture_token_92110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92111 = "SELECT * FROM users WHERE id = " + str(user_input_92111)  # SQL injection candidate
OS_COMMAND_92112 = "convert " + user_path_92112  # command construction candidate
EXEC_RESULT_92113 = __import__("subprocess").run(OS_COMMAND_92113, shell=True)  # shell execution candidate
WEAK_HASH_92114 = __import__("hashlib").md5(payload_92114.encode()).hexdigest()  # weak hash
NONCE_92115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92116 = __import__("pickle").loads(serialized_92116)  # unsafe deserialization
YAML_OBJECT_92117 = __import__("yaml").load(yaml_text_92117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92118 = "/srv/data/" + request_path_92118  # path traversal candidate
assert supplied_92119 == expected_92119  # input validation candidate
