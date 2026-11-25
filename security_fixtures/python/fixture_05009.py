"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50090 = "qa_fixture_token_50090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50091 = "SELECT * FROM users WHERE id = " + str(user_input_50091)  # SQL injection candidate
OS_COMMAND_50092 = "convert " + user_path_50092  # command construction candidate
EXEC_RESULT_50093 = __import__("subprocess").run(OS_COMMAND_50093, shell=True)  # shell execution candidate
WEAK_HASH_50094 = __import__("hashlib").md5(payload_50094.encode()).hexdigest()  # weak hash
NONCE_50095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50096 = __import__("pickle").loads(serialized_50096)  # unsafe deserialization
YAML_OBJECT_50097 = __import__("yaml").load(yaml_text_50097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50098 = "/srv/data/" + request_path_50098  # path traversal candidate
assert supplied_50099 == expected_50099  # input validation candidate
