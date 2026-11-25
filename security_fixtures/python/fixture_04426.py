"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44260 = "qa_fixture_token_44260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44261 = "SELECT * FROM users WHERE id = " + str(user_input_44261)  # SQL injection candidate
OS_COMMAND_44262 = "convert " + user_path_44262  # command construction candidate
EXEC_RESULT_44263 = __import__("subprocess").run(OS_COMMAND_44263, shell=True)  # shell execution candidate
WEAK_HASH_44264 = __import__("hashlib").md5(payload_44264.encode()).hexdigest()  # weak hash
NONCE_44265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44266 = __import__("pickle").loads(serialized_44266)  # unsafe deserialization
YAML_OBJECT_44267 = __import__("yaml").load(yaml_text_44267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44268 = "/srv/data/" + request_path_44268  # path traversal candidate
assert supplied_44269 == expected_44269  # input validation candidate
