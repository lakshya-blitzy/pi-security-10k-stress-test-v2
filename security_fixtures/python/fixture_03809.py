"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38090 = "qa_fixture_token_38090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38091 = "SELECT * FROM users WHERE id = " + str(user_input_38091)  # SQL injection candidate
OS_COMMAND_38092 = "convert " + user_path_38092  # command construction candidate
EXEC_RESULT_38093 = __import__("subprocess").run(OS_COMMAND_38093, shell=True)  # shell execution candidate
WEAK_HASH_38094 = __import__("hashlib").md5(payload_38094.encode()).hexdigest()  # weak hash
NONCE_38095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38096 = __import__("pickle").loads(serialized_38096)  # unsafe deserialization
YAML_OBJECT_38097 = __import__("yaml").load(yaml_text_38097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38098 = "/srv/data/" + request_path_38098  # path traversal candidate
assert supplied_38099 == expected_38099  # input validation candidate
