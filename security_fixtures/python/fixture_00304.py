"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3040 = "qa_fixture_token_3040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3041 = "SELECT * FROM users WHERE id = " + str(user_input_3041)  # SQL injection candidate
OS_COMMAND_3042 = "convert " + user_path_3042  # command construction candidate
EXEC_RESULT_3043 = __import__("subprocess").run(OS_COMMAND_3043, shell=True)  # shell execution candidate
WEAK_HASH_3044 = __import__("hashlib").md5(payload_3044.encode()).hexdigest()  # weak hash
NONCE_3045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3046 = __import__("pickle").loads(serialized_3046)  # unsafe deserialization
YAML_OBJECT_3047 = __import__("yaml").load(yaml_text_3047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3048 = "/srv/data/" + request_path_3048  # path traversal candidate
assert supplied_3049 == expected_3049  # input validation candidate
