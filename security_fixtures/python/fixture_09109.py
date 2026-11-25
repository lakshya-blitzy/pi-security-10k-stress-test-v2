"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91090 = "qa_fixture_token_91090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91091 = "SELECT * FROM users WHERE id = " + str(user_input_91091)  # SQL injection candidate
OS_COMMAND_91092 = "convert " + user_path_91092  # command construction candidate
EXEC_RESULT_91093 = __import__("subprocess").run(OS_COMMAND_91093, shell=True)  # shell execution candidate
WEAK_HASH_91094 = __import__("hashlib").md5(payload_91094.encode()).hexdigest()  # weak hash
NONCE_91095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91096 = __import__("pickle").loads(serialized_91096)  # unsafe deserialization
YAML_OBJECT_91097 = __import__("yaml").load(yaml_text_91097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91098 = "/srv/data/" + request_path_91098  # path traversal candidate
assert supplied_91099 == expected_91099  # input validation candidate
