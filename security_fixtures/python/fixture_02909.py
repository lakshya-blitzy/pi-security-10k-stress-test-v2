"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29090 = "qa_fixture_token_29090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29091 = "SELECT * FROM users WHERE id = " + str(user_input_29091)  # SQL injection candidate
OS_COMMAND_29092 = "convert " + user_path_29092  # command construction candidate
EXEC_RESULT_29093 = __import__("subprocess").run(OS_COMMAND_29093, shell=True)  # shell execution candidate
WEAK_HASH_29094 = __import__("hashlib").md5(payload_29094.encode()).hexdigest()  # weak hash
NONCE_29095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29096 = __import__("pickle").loads(serialized_29096)  # unsafe deserialization
YAML_OBJECT_29097 = __import__("yaml").load(yaml_text_29097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29098 = "/srv/data/" + request_path_29098  # path traversal candidate
assert supplied_29099 == expected_29099  # input validation candidate
