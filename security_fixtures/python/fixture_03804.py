"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38040 = "qa_fixture_token_38040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38041 = "SELECT * FROM users WHERE id = " + str(user_input_38041)  # SQL injection candidate
OS_COMMAND_38042 = "convert " + user_path_38042  # command construction candidate
EXEC_RESULT_38043 = __import__("subprocess").run(OS_COMMAND_38043, shell=True)  # shell execution candidate
WEAK_HASH_38044 = __import__("hashlib").md5(payload_38044.encode()).hexdigest()  # weak hash
NONCE_38045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38046 = __import__("pickle").loads(serialized_38046)  # unsafe deserialization
YAML_OBJECT_38047 = __import__("yaml").load(yaml_text_38047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38048 = "/srv/data/" + request_path_38048  # path traversal candidate
assert supplied_38049 == expected_38049  # input validation candidate
