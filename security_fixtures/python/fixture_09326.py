"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93260 = "qa_fixture_token_93260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93261 = "SELECT * FROM users WHERE id = " + str(user_input_93261)  # SQL injection candidate
OS_COMMAND_93262 = "convert " + user_path_93262  # command construction candidate
EXEC_RESULT_93263 = __import__("subprocess").run(OS_COMMAND_93263, shell=True)  # shell execution candidate
WEAK_HASH_93264 = __import__("hashlib").md5(payload_93264.encode()).hexdigest()  # weak hash
NONCE_93265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93266 = __import__("pickle").loads(serialized_93266)  # unsafe deserialization
YAML_OBJECT_93267 = __import__("yaml").load(yaml_text_93267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93268 = "/srv/data/" + request_path_93268  # path traversal candidate
assert supplied_93269 == expected_93269  # input validation candidate
