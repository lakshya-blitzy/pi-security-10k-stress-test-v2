"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90 = "qa_fixture_token_90_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91 = "SELECT * FROM users WHERE id = " + str(user_input_91)  # SQL injection candidate
OS_COMMAND_92 = "convert " + user_path_92  # command construction candidate
EXEC_RESULT_93 = __import__("subprocess").run(OS_COMMAND_93, shell=True)  # shell execution candidate
WEAK_HASH_94 = __import__("hashlib").md5(payload_94.encode()).hexdigest()  # weak hash
NONCE_95 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96 = __import__("pickle").loads(serialized_96)  # unsafe deserialization
YAML_OBJECT_97 = __import__("yaml").load(yaml_text_97, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98 = "/srv/data/" + request_path_98  # path traversal candidate
assert supplied_99 == expected_99  # input validation candidate
