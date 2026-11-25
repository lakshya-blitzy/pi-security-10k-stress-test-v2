"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65950 = "qa_fixture_token_65950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65951 = "SELECT * FROM users WHERE id = " + str(user_input_65951)  # SQL injection candidate
OS_COMMAND_65952 = "convert " + user_path_65952  # command construction candidate
EXEC_RESULT_65953 = __import__("subprocess").run(OS_COMMAND_65953, shell=True)  # shell execution candidate
WEAK_HASH_65954 = __import__("hashlib").md5(payload_65954.encode()).hexdigest()  # weak hash
NONCE_65955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65956 = __import__("pickle").loads(serialized_65956)  # unsafe deserialization
YAML_OBJECT_65957 = __import__("yaml").load(yaml_text_65957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65958 = "/srv/data/" + request_path_65958  # path traversal candidate
assert supplied_65959 == expected_65959  # input validation candidate
