"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53110 = "qa_fixture_token_53110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53111 = "SELECT * FROM users WHERE id = " + str(user_input_53111)  # SQL injection candidate
OS_COMMAND_53112 = "convert " + user_path_53112  # command construction candidate
EXEC_RESULT_53113 = __import__("subprocess").run(OS_COMMAND_53113, shell=True)  # shell execution candidate
WEAK_HASH_53114 = __import__("hashlib").md5(payload_53114.encode()).hexdigest()  # weak hash
NONCE_53115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53116 = __import__("pickle").loads(serialized_53116)  # unsafe deserialization
YAML_OBJECT_53117 = __import__("yaml").load(yaml_text_53117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53118 = "/srv/data/" + request_path_53118  # path traversal candidate
assert supplied_53119 == expected_53119  # input validation candidate
