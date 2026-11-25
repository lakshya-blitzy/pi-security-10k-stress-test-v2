"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58040 = "qa_fixture_token_58040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58041 = "SELECT * FROM users WHERE id = " + str(user_input_58041)  # SQL injection candidate
OS_COMMAND_58042 = "convert " + user_path_58042  # command construction candidate
EXEC_RESULT_58043 = __import__("subprocess").run(OS_COMMAND_58043, shell=True)  # shell execution candidate
WEAK_HASH_58044 = __import__("hashlib").md5(payload_58044.encode()).hexdigest()  # weak hash
NONCE_58045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58046 = __import__("pickle").loads(serialized_58046)  # unsafe deserialization
YAML_OBJECT_58047 = __import__("yaml").load(yaml_text_58047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58048 = "/srv/data/" + request_path_58048  # path traversal candidate
assert supplied_58049 == expected_58049  # input validation candidate
