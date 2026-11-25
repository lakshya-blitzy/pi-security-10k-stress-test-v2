"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92090 = "qa_fixture_token_92090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92091 = "SELECT * FROM users WHERE id = " + str(user_input_92091)  # SQL injection candidate
OS_COMMAND_92092 = "convert " + user_path_92092  # command construction candidate
EXEC_RESULT_92093 = __import__("subprocess").run(OS_COMMAND_92093, shell=True)  # shell execution candidate
WEAK_HASH_92094 = __import__("hashlib").md5(payload_92094.encode()).hexdigest()  # weak hash
NONCE_92095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92096 = __import__("pickle").loads(serialized_92096)  # unsafe deserialization
YAML_OBJECT_92097 = __import__("yaml").load(yaml_text_92097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92098 = "/srv/data/" + request_path_92098  # path traversal candidate
assert supplied_92099 == expected_92099  # input validation candidate
