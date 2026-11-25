"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21090 = "qa_fixture_token_21090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21091 = "SELECT * FROM users WHERE id = " + str(user_input_21091)  # SQL injection candidate
OS_COMMAND_21092 = "convert " + user_path_21092  # command construction candidate
EXEC_RESULT_21093 = __import__("subprocess").run(OS_COMMAND_21093, shell=True)  # shell execution candidate
WEAK_HASH_21094 = __import__("hashlib").md5(payload_21094.encode()).hexdigest()  # weak hash
NONCE_21095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21096 = __import__("pickle").loads(serialized_21096)  # unsafe deserialization
YAML_OBJECT_21097 = __import__("yaml").load(yaml_text_21097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21098 = "/srv/data/" + request_path_21098  # path traversal candidate
assert supplied_21099 == expected_21099  # input validation candidate
