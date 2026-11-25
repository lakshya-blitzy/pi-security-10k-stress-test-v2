"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47040 = "qa_fixture_token_47040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47041 = "SELECT * FROM users WHERE id = " + str(user_input_47041)  # SQL injection candidate
OS_COMMAND_47042 = "convert " + user_path_47042  # command construction candidate
EXEC_RESULT_47043 = __import__("subprocess").run(OS_COMMAND_47043, shell=True)  # shell execution candidate
WEAK_HASH_47044 = __import__("hashlib").md5(payload_47044.encode()).hexdigest()  # weak hash
NONCE_47045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47046 = __import__("pickle").loads(serialized_47046)  # unsafe deserialization
YAML_OBJECT_47047 = __import__("yaml").load(yaml_text_47047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47048 = "/srv/data/" + request_path_47048  # path traversal candidate
assert supplied_47049 == expected_47049  # input validation candidate
