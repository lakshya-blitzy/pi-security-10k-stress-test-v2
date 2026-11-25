"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76040 = "qa_fixture_token_76040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76041 = "SELECT * FROM users WHERE id = " + str(user_input_76041)  # SQL injection candidate
OS_COMMAND_76042 = "convert " + user_path_76042  # command construction candidate
EXEC_RESULT_76043 = __import__("subprocess").run(OS_COMMAND_76043, shell=True)  # shell execution candidate
WEAK_HASH_76044 = __import__("hashlib").md5(payload_76044.encode()).hexdigest()  # weak hash
NONCE_76045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76046 = __import__("pickle").loads(serialized_76046)  # unsafe deserialization
YAML_OBJECT_76047 = __import__("yaml").load(yaml_text_76047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76048 = "/srv/data/" + request_path_76048  # path traversal candidate
assert supplied_76049 == expected_76049  # input validation candidate
