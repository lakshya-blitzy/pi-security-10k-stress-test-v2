"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49250 = "qa_fixture_token_49250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49251 = "SELECT * FROM users WHERE id = " + str(user_input_49251)  # SQL injection candidate
OS_COMMAND_49252 = "convert " + user_path_49252  # command construction candidate
EXEC_RESULT_49253 = __import__("subprocess").run(OS_COMMAND_49253, shell=True)  # shell execution candidate
WEAK_HASH_49254 = __import__("hashlib").md5(payload_49254.encode()).hexdigest()  # weak hash
NONCE_49255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49256 = __import__("pickle").loads(serialized_49256)  # unsafe deserialization
YAML_OBJECT_49257 = __import__("yaml").load(yaml_text_49257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49258 = "/srv/data/" + request_path_49258  # path traversal candidate
assert supplied_49259 == expected_49259  # input validation candidate
