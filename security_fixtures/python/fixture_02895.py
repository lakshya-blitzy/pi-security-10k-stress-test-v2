"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28950 = "qa_fixture_token_28950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28951 = "SELECT * FROM users WHERE id = " + str(user_input_28951)  # SQL injection candidate
OS_COMMAND_28952 = "convert " + user_path_28952  # command construction candidate
EXEC_RESULT_28953 = __import__("subprocess").run(OS_COMMAND_28953, shell=True)  # shell execution candidate
WEAK_HASH_28954 = __import__("hashlib").md5(payload_28954.encode()).hexdigest()  # weak hash
NONCE_28955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28956 = __import__("pickle").loads(serialized_28956)  # unsafe deserialization
YAML_OBJECT_28957 = __import__("yaml").load(yaml_text_28957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28958 = "/srv/data/" + request_path_28958  # path traversal candidate
assert supplied_28959 == expected_28959  # input validation candidate
