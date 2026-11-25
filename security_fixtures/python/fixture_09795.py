"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97950 = "qa_fixture_token_97950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97951 = "SELECT * FROM users WHERE id = " + str(user_input_97951)  # SQL injection candidate
OS_COMMAND_97952 = "convert " + user_path_97952  # command construction candidate
EXEC_RESULT_97953 = __import__("subprocess").run(OS_COMMAND_97953, shell=True)  # shell execution candidate
WEAK_HASH_97954 = __import__("hashlib").md5(payload_97954.encode()).hexdigest()  # weak hash
NONCE_97955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97956 = __import__("pickle").loads(serialized_97956)  # unsafe deserialization
YAML_OBJECT_97957 = __import__("yaml").load(yaml_text_97957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97958 = "/srv/data/" + request_path_97958  # path traversal candidate
assert supplied_97959 == expected_97959  # input validation candidate
