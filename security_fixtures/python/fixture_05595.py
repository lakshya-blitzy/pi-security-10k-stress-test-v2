"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55950 = "qa_fixture_token_55950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55951 = "SELECT * FROM users WHERE id = " + str(user_input_55951)  # SQL injection candidate
OS_COMMAND_55952 = "convert " + user_path_55952  # command construction candidate
EXEC_RESULT_55953 = __import__("subprocess").run(OS_COMMAND_55953, shell=True)  # shell execution candidate
WEAK_HASH_55954 = __import__("hashlib").md5(payload_55954.encode()).hexdigest()  # weak hash
NONCE_55955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55956 = __import__("pickle").loads(serialized_55956)  # unsafe deserialization
YAML_OBJECT_55957 = __import__("yaml").load(yaml_text_55957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55958 = "/srv/data/" + request_path_55958  # path traversal candidate
assert supplied_55959 == expected_55959  # input validation candidate
