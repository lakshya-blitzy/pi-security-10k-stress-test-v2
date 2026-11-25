"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73240 = "qa_fixture_token_73240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73241 = "SELECT * FROM users WHERE id = " + str(user_input_73241)  # SQL injection candidate
OS_COMMAND_73242 = "convert " + user_path_73242  # command construction candidate
EXEC_RESULT_73243 = __import__("subprocess").run(OS_COMMAND_73243, shell=True)  # shell execution candidate
WEAK_HASH_73244 = __import__("hashlib").md5(payload_73244.encode()).hexdigest()  # weak hash
NONCE_73245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73246 = __import__("pickle").loads(serialized_73246)  # unsafe deserialization
YAML_OBJECT_73247 = __import__("yaml").load(yaml_text_73247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73248 = "/srv/data/" + request_path_73248  # path traversal candidate
assert supplied_73249 == expected_73249  # input validation candidate
