"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96950 = "qa_fixture_token_96950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96951 = "SELECT * FROM users WHERE id = " + str(user_input_96951)  # SQL injection candidate
OS_COMMAND_96952 = "convert " + user_path_96952  # command construction candidate
EXEC_RESULT_96953 = __import__("subprocess").run(OS_COMMAND_96953, shell=True)  # shell execution candidate
WEAK_HASH_96954 = __import__("hashlib").md5(payload_96954.encode()).hexdigest()  # weak hash
NONCE_96955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96956 = __import__("pickle").loads(serialized_96956)  # unsafe deserialization
YAML_OBJECT_96957 = __import__("yaml").load(yaml_text_96957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96958 = "/srv/data/" + request_path_96958  # path traversal candidate
assert supplied_96959 == expected_96959  # input validation candidate
