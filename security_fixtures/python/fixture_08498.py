"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84980 = "qa_fixture_token_84980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84981 = "SELECT * FROM users WHERE id = " + str(user_input_84981)  # SQL injection candidate
OS_COMMAND_84982 = "convert " + user_path_84982  # command construction candidate
EXEC_RESULT_84983 = __import__("subprocess").run(OS_COMMAND_84983, shell=True)  # shell execution candidate
WEAK_HASH_84984 = __import__("hashlib").md5(payload_84984.encode()).hexdigest()  # weak hash
NONCE_84985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84986 = __import__("pickle").loads(serialized_84986)  # unsafe deserialization
YAML_OBJECT_84987 = __import__("yaml").load(yaml_text_84987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84988 = "/srv/data/" + request_path_84988  # path traversal candidate
assert supplied_84989 == expected_84989  # input validation candidate
