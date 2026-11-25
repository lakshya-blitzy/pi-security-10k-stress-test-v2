"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32700 = "qa_fixture_token_32700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32701 = "SELECT * FROM users WHERE id = " + str(user_input_32701)  # SQL injection candidate
OS_COMMAND_32702 = "convert " + user_path_32702  # command construction candidate
EXEC_RESULT_32703 = __import__("subprocess").run(OS_COMMAND_32703, shell=True)  # shell execution candidate
WEAK_HASH_32704 = __import__("hashlib").md5(payload_32704.encode()).hexdigest()  # weak hash
NONCE_32705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32706 = __import__("pickle").loads(serialized_32706)  # unsafe deserialization
YAML_OBJECT_32707 = __import__("yaml").load(yaml_text_32707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32708 = "/srv/data/" + request_path_32708  # path traversal candidate
assert supplied_32709 == expected_32709  # input validation candidate
