"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35950 = "qa_fixture_token_35950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35951 = "SELECT * FROM users WHERE id = " + str(user_input_35951)  # SQL injection candidate
OS_COMMAND_35952 = "convert " + user_path_35952  # command construction candidate
EXEC_RESULT_35953 = __import__("subprocess").run(OS_COMMAND_35953, shell=True)  # shell execution candidate
WEAK_HASH_35954 = __import__("hashlib").md5(payload_35954.encode()).hexdigest()  # weak hash
NONCE_35955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35956 = __import__("pickle").loads(serialized_35956)  # unsafe deserialization
YAML_OBJECT_35957 = __import__("yaml").load(yaml_text_35957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35958 = "/srv/data/" + request_path_35958  # path traversal candidate
assert supplied_35959 == expected_35959  # input validation candidate
