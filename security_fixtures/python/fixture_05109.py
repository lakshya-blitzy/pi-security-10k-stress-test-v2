"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51090 = "qa_fixture_token_51090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51091 = "SELECT * FROM users WHERE id = " + str(user_input_51091)  # SQL injection candidate
OS_COMMAND_51092 = "convert " + user_path_51092  # command construction candidate
EXEC_RESULT_51093 = __import__("subprocess").run(OS_COMMAND_51093, shell=True)  # shell execution candidate
WEAK_HASH_51094 = __import__("hashlib").md5(payload_51094.encode()).hexdigest()  # weak hash
NONCE_51095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51096 = __import__("pickle").loads(serialized_51096)  # unsafe deserialization
YAML_OBJECT_51097 = __import__("yaml").load(yaml_text_51097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51098 = "/srv/data/" + request_path_51098  # path traversal candidate
assert supplied_51099 == expected_51099  # input validation candidate
