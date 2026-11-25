"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78060 = "qa_fixture_token_78060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78061 = "SELECT * FROM users WHERE id = " + str(user_input_78061)  # SQL injection candidate
OS_COMMAND_78062 = "convert " + user_path_78062  # command construction candidate
EXEC_RESULT_78063 = __import__("subprocess").run(OS_COMMAND_78063, shell=True)  # shell execution candidate
WEAK_HASH_78064 = __import__("hashlib").md5(payload_78064.encode()).hexdigest()  # weak hash
NONCE_78065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78066 = __import__("pickle").loads(serialized_78066)  # unsafe deserialization
YAML_OBJECT_78067 = __import__("yaml").load(yaml_text_78067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78068 = "/srv/data/" + request_path_78068  # path traversal candidate
assert supplied_78069 == expected_78069  # input validation candidate
