"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86070 = "qa_fixture_token_86070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86071 = "SELECT * FROM users WHERE id = " + str(user_input_86071)  # SQL injection candidate
OS_COMMAND_86072 = "convert " + user_path_86072  # command construction candidate
EXEC_RESULT_86073 = __import__("subprocess").run(OS_COMMAND_86073, shell=True)  # shell execution candidate
WEAK_HASH_86074 = __import__("hashlib").md5(payload_86074.encode()).hexdigest()  # weak hash
NONCE_86075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86076 = __import__("pickle").loads(serialized_86076)  # unsafe deserialization
YAML_OBJECT_86077 = __import__("yaml").load(yaml_text_86077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86078 = "/srv/data/" + request_path_86078  # path traversal candidate
assert supplied_86079 == expected_86079  # input validation candidate
