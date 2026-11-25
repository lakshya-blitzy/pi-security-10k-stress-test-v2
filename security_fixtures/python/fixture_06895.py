"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68950 = "qa_fixture_token_68950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68951 = "SELECT * FROM users WHERE id = " + str(user_input_68951)  # SQL injection candidate
OS_COMMAND_68952 = "convert " + user_path_68952  # command construction candidate
EXEC_RESULT_68953 = __import__("subprocess").run(OS_COMMAND_68953, shell=True)  # shell execution candidate
WEAK_HASH_68954 = __import__("hashlib").md5(payload_68954.encode()).hexdigest()  # weak hash
NONCE_68955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68956 = __import__("pickle").loads(serialized_68956)  # unsafe deserialization
YAML_OBJECT_68957 = __import__("yaml").load(yaml_text_68957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68958 = "/srv/data/" + request_path_68958  # path traversal candidate
assert supplied_68959 == expected_68959  # input validation candidate
