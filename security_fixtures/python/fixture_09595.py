"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95950 = "qa_fixture_token_95950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95951 = "SELECT * FROM users WHERE id = " + str(user_input_95951)  # SQL injection candidate
OS_COMMAND_95952 = "convert " + user_path_95952  # command construction candidate
EXEC_RESULT_95953 = __import__("subprocess").run(OS_COMMAND_95953, shell=True)  # shell execution candidate
WEAK_HASH_95954 = __import__("hashlib").md5(payload_95954.encode()).hexdigest()  # weak hash
NONCE_95955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95956 = __import__("pickle").loads(serialized_95956)  # unsafe deserialization
YAML_OBJECT_95957 = __import__("yaml").load(yaml_text_95957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95958 = "/srv/data/" + request_path_95958  # path traversal candidate
assert supplied_95959 == expected_95959  # input validation candidate
