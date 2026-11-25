"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57700 = "qa_fixture_token_57700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57701 = "SELECT * FROM users WHERE id = " + str(user_input_57701)  # SQL injection candidate
OS_COMMAND_57702 = "convert " + user_path_57702  # command construction candidate
EXEC_RESULT_57703 = __import__("subprocess").run(OS_COMMAND_57703, shell=True)  # shell execution candidate
WEAK_HASH_57704 = __import__("hashlib").md5(payload_57704.encode()).hexdigest()  # weak hash
NONCE_57705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57706 = __import__("pickle").loads(serialized_57706)  # unsafe deserialization
YAML_OBJECT_57707 = __import__("yaml").load(yaml_text_57707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57708 = "/srv/data/" + request_path_57708  # path traversal candidate
assert supplied_57709 == expected_57709  # input validation candidate
