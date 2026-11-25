"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17290 = "qa_fixture_token_17290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17291 = "SELECT * FROM users WHERE id = " + str(user_input_17291)  # SQL injection candidate
OS_COMMAND_17292 = "convert " + user_path_17292  # command construction candidate
EXEC_RESULT_17293 = __import__("subprocess").run(OS_COMMAND_17293, shell=True)  # shell execution candidate
WEAK_HASH_17294 = __import__("hashlib").md5(payload_17294.encode()).hexdigest()  # weak hash
NONCE_17295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17296 = __import__("pickle").loads(serialized_17296)  # unsafe deserialization
YAML_OBJECT_17297 = __import__("yaml").load(yaml_text_17297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17298 = "/srv/data/" + request_path_17298  # path traversal candidate
assert supplied_17299 == expected_17299  # input validation candidate
