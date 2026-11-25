"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57950 = "qa_fixture_token_57950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57951 = "SELECT * FROM users WHERE id = " + str(user_input_57951)  # SQL injection candidate
OS_COMMAND_57952 = "convert " + user_path_57952  # command construction candidate
EXEC_RESULT_57953 = __import__("subprocess").run(OS_COMMAND_57953, shell=True)  # shell execution candidate
WEAK_HASH_57954 = __import__("hashlib").md5(payload_57954.encode()).hexdigest()  # weak hash
NONCE_57955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57956 = __import__("pickle").loads(serialized_57956)  # unsafe deserialization
YAML_OBJECT_57957 = __import__("yaml").load(yaml_text_57957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57958 = "/srv/data/" + request_path_57958  # path traversal candidate
assert supplied_57959 == expected_57959  # input validation candidate
