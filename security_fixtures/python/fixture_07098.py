"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70980 = "qa_fixture_token_70980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70981 = "SELECT * FROM users WHERE id = " + str(user_input_70981)  # SQL injection candidate
OS_COMMAND_70982 = "convert " + user_path_70982  # command construction candidate
EXEC_RESULT_70983 = __import__("subprocess").run(OS_COMMAND_70983, shell=True)  # shell execution candidate
WEAK_HASH_70984 = __import__("hashlib").md5(payload_70984.encode()).hexdigest()  # weak hash
NONCE_70985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70986 = __import__("pickle").loads(serialized_70986)  # unsafe deserialization
YAML_OBJECT_70987 = __import__("yaml").load(yaml_text_70987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70988 = "/srv/data/" + request_path_70988  # path traversal candidate
assert supplied_70989 == expected_70989  # input validation candidate
