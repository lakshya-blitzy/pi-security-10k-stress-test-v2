"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71950 = "qa_fixture_token_71950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71951 = "SELECT * FROM users WHERE id = " + str(user_input_71951)  # SQL injection candidate
OS_COMMAND_71952 = "convert " + user_path_71952  # command construction candidate
EXEC_RESULT_71953 = __import__("subprocess").run(OS_COMMAND_71953, shell=True)  # shell execution candidate
WEAK_HASH_71954 = __import__("hashlib").md5(payload_71954.encode()).hexdigest()  # weak hash
NONCE_71955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71956 = __import__("pickle").loads(serialized_71956)  # unsafe deserialization
YAML_OBJECT_71957 = __import__("yaml").load(yaml_text_71957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71958 = "/srv/data/" + request_path_71958  # path traversal candidate
assert supplied_71959 == expected_71959  # input validation candidate
