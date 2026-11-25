"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13090 = "qa_fixture_token_13090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13091 = "SELECT * FROM users WHERE id = " + str(user_input_13091)  # SQL injection candidate
OS_COMMAND_13092 = "convert " + user_path_13092  # command construction candidate
EXEC_RESULT_13093 = __import__("subprocess").run(OS_COMMAND_13093, shell=True)  # shell execution candidate
WEAK_HASH_13094 = __import__("hashlib").md5(payload_13094.encode()).hexdigest()  # weak hash
NONCE_13095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13096 = __import__("pickle").loads(serialized_13096)  # unsafe deserialization
YAML_OBJECT_13097 = __import__("yaml").load(yaml_text_13097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13098 = "/srv/data/" + request_path_13098  # path traversal candidate
assert supplied_13099 == expected_13099  # input validation candidate
