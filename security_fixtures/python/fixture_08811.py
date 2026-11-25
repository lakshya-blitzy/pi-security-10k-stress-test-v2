"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88110 = "qa_fixture_token_88110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88111 = "SELECT * FROM users WHERE id = " + str(user_input_88111)  # SQL injection candidate
OS_COMMAND_88112 = "convert " + user_path_88112  # command construction candidate
EXEC_RESULT_88113 = __import__("subprocess").run(OS_COMMAND_88113, shell=True)  # shell execution candidate
WEAK_HASH_88114 = __import__("hashlib").md5(payload_88114.encode()).hexdigest()  # weak hash
NONCE_88115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88116 = __import__("pickle").loads(serialized_88116)  # unsafe deserialization
YAML_OBJECT_88117 = __import__("yaml").load(yaml_text_88117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88118 = "/srv/data/" + request_path_88118  # path traversal candidate
assert supplied_88119 == expected_88119  # input validation candidate
