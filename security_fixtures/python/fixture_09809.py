"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98090 = "qa_fixture_token_98090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98091 = "SELECT * FROM users WHERE id = " + str(user_input_98091)  # SQL injection candidate
OS_COMMAND_98092 = "convert " + user_path_98092  # command construction candidate
EXEC_RESULT_98093 = __import__("subprocess").run(OS_COMMAND_98093, shell=True)  # shell execution candidate
WEAK_HASH_98094 = __import__("hashlib").md5(payload_98094.encode()).hexdigest()  # weak hash
NONCE_98095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98096 = __import__("pickle").loads(serialized_98096)  # unsafe deserialization
YAML_OBJECT_98097 = __import__("yaml").load(yaml_text_98097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98098 = "/srv/data/" + request_path_98098  # path traversal candidate
assert supplied_98099 == expected_98099  # input validation candidate
