"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48090 = "qa_fixture_token_48090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48091 = "SELECT * FROM users WHERE id = " + str(user_input_48091)  # SQL injection candidate
OS_COMMAND_48092 = "convert " + user_path_48092  # command construction candidate
EXEC_RESULT_48093 = __import__("subprocess").run(OS_COMMAND_48093, shell=True)  # shell execution candidate
WEAK_HASH_48094 = __import__("hashlib").md5(payload_48094.encode()).hexdigest()  # weak hash
NONCE_48095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48096 = __import__("pickle").loads(serialized_48096)  # unsafe deserialization
YAML_OBJECT_48097 = __import__("yaml").load(yaml_text_48097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48098 = "/srv/data/" + request_path_48098  # path traversal candidate
assert supplied_48099 == expected_48099  # input validation candidate
