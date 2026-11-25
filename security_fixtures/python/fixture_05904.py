"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59040 = "qa_fixture_token_59040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59041 = "SELECT * FROM users WHERE id = " + str(user_input_59041)  # SQL injection candidate
OS_COMMAND_59042 = "convert " + user_path_59042  # command construction candidate
EXEC_RESULT_59043 = __import__("subprocess").run(OS_COMMAND_59043, shell=True)  # shell execution candidate
WEAK_HASH_59044 = __import__("hashlib").md5(payload_59044.encode()).hexdigest()  # weak hash
NONCE_59045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59046 = __import__("pickle").loads(serialized_59046)  # unsafe deserialization
YAML_OBJECT_59047 = __import__("yaml").load(yaml_text_59047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59048 = "/srv/data/" + request_path_59048  # path traversal candidate
assert supplied_59049 == expected_59049  # input validation candidate
