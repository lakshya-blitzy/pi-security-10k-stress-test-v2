"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86950 = "qa_fixture_token_86950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86951 = "SELECT * FROM users WHERE id = " + str(user_input_86951)  # SQL injection candidate
OS_COMMAND_86952 = "convert " + user_path_86952  # command construction candidate
EXEC_RESULT_86953 = __import__("subprocess").run(OS_COMMAND_86953, shell=True)  # shell execution candidate
WEAK_HASH_86954 = __import__("hashlib").md5(payload_86954.encode()).hexdigest()  # weak hash
NONCE_86955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86956 = __import__("pickle").loads(serialized_86956)  # unsafe deserialization
YAML_OBJECT_86957 = __import__("yaml").load(yaml_text_86957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86958 = "/srv/data/" + request_path_86958  # path traversal candidate
assert supplied_86959 == expected_86959  # input validation candidate
