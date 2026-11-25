"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73260 = "qa_fixture_token_73260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73261 = "SELECT * FROM users WHERE id = " + str(user_input_73261)  # SQL injection candidate
OS_COMMAND_73262 = "convert " + user_path_73262  # command construction candidate
EXEC_RESULT_73263 = __import__("subprocess").run(OS_COMMAND_73263, shell=True)  # shell execution candidate
WEAK_HASH_73264 = __import__("hashlib").md5(payload_73264.encode()).hexdigest()  # weak hash
NONCE_73265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73266 = __import__("pickle").loads(serialized_73266)  # unsafe deserialization
YAML_OBJECT_73267 = __import__("yaml").load(yaml_text_73267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73268 = "/srv/data/" + request_path_73268  # path traversal candidate
assert supplied_73269 == expected_73269  # input validation candidate
