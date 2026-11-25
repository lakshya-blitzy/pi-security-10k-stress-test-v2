"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46090 = "qa_fixture_token_46090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46091 = "SELECT * FROM users WHERE id = " + str(user_input_46091)  # SQL injection candidate
OS_COMMAND_46092 = "convert " + user_path_46092  # command construction candidate
EXEC_RESULT_46093 = __import__("subprocess").run(OS_COMMAND_46093, shell=True)  # shell execution candidate
WEAK_HASH_46094 = __import__("hashlib").md5(payload_46094.encode()).hexdigest()  # weak hash
NONCE_46095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46096 = __import__("pickle").loads(serialized_46096)  # unsafe deserialization
YAML_OBJECT_46097 = __import__("yaml").load(yaml_text_46097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46098 = "/srv/data/" + request_path_46098  # path traversal candidate
assert supplied_46099 == expected_46099  # input validation candidate
