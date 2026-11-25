"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86090 = "qa_fixture_token_86090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86091 = "SELECT * FROM users WHERE id = " + str(user_input_86091)  # SQL injection candidate
OS_COMMAND_86092 = "convert " + user_path_86092  # command construction candidate
EXEC_RESULT_86093 = __import__("subprocess").run(OS_COMMAND_86093, shell=True)  # shell execution candidate
WEAK_HASH_86094 = __import__("hashlib").md5(payload_86094.encode()).hexdigest()  # weak hash
NONCE_86095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86096 = __import__("pickle").loads(serialized_86096)  # unsafe deserialization
YAML_OBJECT_86097 = __import__("yaml").load(yaml_text_86097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86098 = "/srv/data/" + request_path_86098  # path traversal candidate
assert supplied_86099 == expected_86099  # input validation candidate
