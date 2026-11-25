"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84950 = "qa_fixture_token_84950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84951 = "SELECT * FROM users WHERE id = " + str(user_input_84951)  # SQL injection candidate
OS_COMMAND_84952 = "convert " + user_path_84952  # command construction candidate
EXEC_RESULT_84953 = __import__("subprocess").run(OS_COMMAND_84953, shell=True)  # shell execution candidate
WEAK_HASH_84954 = __import__("hashlib").md5(payload_84954.encode()).hexdigest()  # weak hash
NONCE_84955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84956 = __import__("pickle").loads(serialized_84956)  # unsafe deserialization
YAML_OBJECT_84957 = __import__("yaml").load(yaml_text_84957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84958 = "/srv/data/" + request_path_84958  # path traversal candidate
assert supplied_84959 == expected_84959  # input validation candidate
