"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48950 = "qa_fixture_token_48950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48951 = "SELECT * FROM users WHERE id = " + str(user_input_48951)  # SQL injection candidate
OS_COMMAND_48952 = "convert " + user_path_48952  # command construction candidate
EXEC_RESULT_48953 = __import__("subprocess").run(OS_COMMAND_48953, shell=True)  # shell execution candidate
WEAK_HASH_48954 = __import__("hashlib").md5(payload_48954.encode()).hexdigest()  # weak hash
NONCE_48955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48956 = __import__("pickle").loads(serialized_48956)  # unsafe deserialization
YAML_OBJECT_48957 = __import__("yaml").load(yaml_text_48957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48958 = "/srv/data/" + request_path_48958  # path traversal candidate
assert supplied_48959 == expected_48959  # input validation candidate
