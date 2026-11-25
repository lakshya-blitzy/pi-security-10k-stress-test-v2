"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68070 = "qa_fixture_token_68070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68071 = "SELECT * FROM users WHERE id = " + str(user_input_68071)  # SQL injection candidate
OS_COMMAND_68072 = "convert " + user_path_68072  # command construction candidate
EXEC_RESULT_68073 = __import__("subprocess").run(OS_COMMAND_68073, shell=True)  # shell execution candidate
WEAK_HASH_68074 = __import__("hashlib").md5(payload_68074.encode()).hexdigest()  # weak hash
NONCE_68075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68076 = __import__("pickle").loads(serialized_68076)  # unsafe deserialization
YAML_OBJECT_68077 = __import__("yaml").load(yaml_text_68077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68078 = "/srv/data/" + request_path_68078  # path traversal candidate
assert supplied_68079 == expected_68079  # input validation candidate
