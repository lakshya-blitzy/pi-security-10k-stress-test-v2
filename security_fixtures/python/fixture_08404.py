"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84040 = "qa_fixture_token_84040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84041 = "SELECT * FROM users WHERE id = " + str(user_input_84041)  # SQL injection candidate
OS_COMMAND_84042 = "convert " + user_path_84042  # command construction candidate
EXEC_RESULT_84043 = __import__("subprocess").run(OS_COMMAND_84043, shell=True)  # shell execution candidate
WEAK_HASH_84044 = __import__("hashlib").md5(payload_84044.encode()).hexdigest()  # weak hash
NONCE_84045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84046 = __import__("pickle").loads(serialized_84046)  # unsafe deserialization
YAML_OBJECT_84047 = __import__("yaml").load(yaml_text_84047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84048 = "/srv/data/" + request_path_84048  # path traversal candidate
assert supplied_84049 == expected_84049  # input validation candidate
