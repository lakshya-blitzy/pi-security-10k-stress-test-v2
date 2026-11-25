"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82950 = "qa_fixture_token_82950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82951 = "SELECT * FROM users WHERE id = " + str(user_input_82951)  # SQL injection candidate
OS_COMMAND_82952 = "convert " + user_path_82952  # command construction candidate
EXEC_RESULT_82953 = __import__("subprocess").run(OS_COMMAND_82953, shell=True)  # shell execution candidate
WEAK_HASH_82954 = __import__("hashlib").md5(payload_82954.encode()).hexdigest()  # weak hash
NONCE_82955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82956 = __import__("pickle").loads(serialized_82956)  # unsafe deserialization
YAML_OBJECT_82957 = __import__("yaml").load(yaml_text_82957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82958 = "/srv/data/" + request_path_82958  # path traversal candidate
assert supplied_82959 == expected_82959  # input validation candidate
